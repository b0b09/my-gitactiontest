import subprocess


def test_sum():
    result = subprocess.run(
        ["python", "sumcheck.py"],
        input="10\n20\n",
        text=True,
        capture_output=True
    )

    assert "sum of a and b 30" in result.stdout
