import csv
import shutil
import subprocess
import sys
from pathlib import Path

from caesar import caesar_encrypt
from password_manager import (
    add_login,
    change_password,
    encrypt_passwords_in_file,
    encrypt_single_pass,
)


ROOT = Path(__file__).resolve().parent


def copy_fixture(tmp_path, fixture_name):
    src = ROOT / fixture_name
    dst = tmp_path / fixture_name
    shutil.copy(src, dst)
    return dst


def read_csv_rows(path):
    with open(path, "r", newline="", encoding="utf-8") as file:
        return [row for row in csv.reader(file) if row]


def run_program(script_name, inputs):
    process = subprocess.Popen(
        [sys.executable, str(ROOT / script_name)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    input_text = "\n".join(inputs)
    stdout, stderr = process.communicate(input=input_text)
    return process.returncode, stdout, stderr


class TestPasswordManager:
    def test_encrypt_single_pass(self, tmp_path):
        password_file = tmp_path / "single.txt"
        password_file.write_text("supersecure\n", encoding="utf-8")

        encrypt_single_pass(str(password_file))

        assert password_file.read_text(encoding="utf-8") == caesar_encrypt("supersecure")

    def test_encrypt_single_pass_with_symbols_and_digits(self, tmp_path):
        password_file = tmp_path / "single_mixed.txt"
        password_file.write_text("A1z-9!\n", encoding="utf-8")

        encrypt_single_pass(str(password_file))

        assert password_file.read_text(encoding="utf-8") == caesar_encrypt("A1z-9!")

    def test_encrypt_passwords_in_file_uses_main_test1(self, tmp_path):
        csv_file = copy_fixture(tmp_path, "main_test1.csv")

        encrypt_passwords_in_file(str(csv_file))
        rows = read_csv_rows(csv_file)

        assert rows[0] == ["website", "username", "password"]
        assert rows[1] == ["alpha-site.com", "alice", caesar_encrypt("plaintextalpha")]
        assert rows[2] == ["beta-site.com", "bob", caesar_encrypt("plaintextbeta")]

    def test_encrypt_passwords_in_file_skips_blank_lines(self, tmp_path):
        csv_file = tmp_path / "with_blanks.csv"
        csv_file.write_text(
            "website,username,password\n"
            "\n"
            "blanksite.com,user1,passwordone\n"
            "\n"
            "othersite.com,user2,passwordtwo\n",
            encoding="utf-8",
        )

        encrypt_passwords_in_file(str(csv_file))
        rows = read_csv_rows(csv_file)

        assert len(rows) == 3
        assert rows[1] == ["blanksite.com", "user1", caesar_encrypt("passwordone")]
        assert rows[2] == ["othersite.com", "user2", caesar_encrypt("passwordtwo")]

    def test_change_password_uses_main_test3(self, tmp_path):
        csv_file = copy_fixture(tmp_path, "main_test3.csv")

        changed = change_password(str(csv_file), "theta-site.com", "ultrasecuretheta99")
        rows = read_csv_rows(csv_file)

        assert changed is True
        assert rows[3] == ["theta-site.com", "tom", caesar_encrypt("ultrasecuretheta99")]

        not_found = change_password(str(csv_file), "missing-site.com", "anypassword123")
        assert not_found is False

    def test_change_password_missing_site_does_not_modify_file(self, tmp_path):
        csv_file = copy_fixture(tmp_path, "main_test3.csv")
        before = read_csv_rows(csv_file)

        changed = change_password(str(csv_file), "not-present.com", "thisislongenough")
        after = read_csv_rows(csv_file)

        assert changed is False
        assert before == after

    def test_add_login_uses_main_test3(self, tmp_path):
        csv_file = copy_fixture(tmp_path, "main_test3.csv")

        add_login(str(csv_file), "kappa-site.com", "kate", "mystrongpass123")
        rows = read_csv_rows(csv_file)

        assert rows[-1] == ["kappa-site.com", "kate", caesar_encrypt("mystrongpass123")]


class TestMainProgram:
    def test_main_encrypts_file_then_quits_using_main_test2(self, tmp_path):
        csv_file = copy_fixture(tmp_path, "main_test2.csv")

        code, stdout, stderr = run_program("main.py", [str(csv_file), "3"])
        rows = read_csv_rows(csv_file)

        assert code == 0
        assert stderr == ""
        assert "Enter the CSV file name:" in stdout
        assert "Options: (1) Change Password, (2) Add Password, (3) Quit:" in stdout
        assert rows[1][2] == caesar_encrypt("plaintextgamma")
        assert rows[2][2] == caesar_encrypt("plaintextdelta")
        assert rows[3][2] == caesar_encrypt("plaintextepsilon")

    def test_main_full_flow_validations_and_updates(self, tmp_path):
        csv_file = copy_fixture(tmp_path, "main_test2.csv")

        code, stdout, stderr = run_program(
            "main.py",
            [
                str(csv_file),
                "1",
                "gamma-site.com short",
                "1",
                "gamma-site.com verysecurepass",
                "2",
                "newsite2 newuser2 short",
                "2",
                "newsite2.com newuser2 newsecurepass2",
                "1",
                "missing.com longenoughpass",
                "9",
                "3",
            ],
        )

        rows = read_csv_rows(csv_file)

        assert code == 0
        assert stderr == ""
        assert "Password is too short!" in stdout
        assert "Password changed." in stdout
        assert "Login added." in stdout
        assert "Website not found! Operation failed." in stdout
        assert "Invalid option selected!" in stdout

        assert rows[1] == ["gamma-site.com", "charlie", caesar_encrypt("verysecurepass")]
        assert rows[2] == ["delta-site.com", "diana", caesar_encrypt("plaintextdelta")]
        assert rows[3] == ["epsilon-site.com", "edward", caesar_encrypt("plaintextepsilon")]
        assert rows[4] == ["newsite2.com", "newuser2", caesar_encrypt("newsecurepass2")]

    def test_main_wrong_format_for_option_1_and_2(self, tmp_path):
        csv_file = copy_fixture(tmp_path, "main_test1.csv")

        code, stdout, stderr = run_program(
            "main.py",
            [
                str(csv_file),
                "1",
                "onlywebsite",
                "2",
                "onlywebsite onlyuser",
                "3",
            ],
        )

        rows = read_csv_rows(csv_file)

        assert code == 0
        assert stderr == ""
        assert stdout.count("Input is in the wrong format!") == 2
        assert len(rows) == 3
        assert rows[1] == ["alpha-site.com", "alice", caesar_encrypt("plaintextalpha")]
        assert rows[2] == ["beta-site.com", "bob", caesar_encrypt("plaintextbeta")]


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])

