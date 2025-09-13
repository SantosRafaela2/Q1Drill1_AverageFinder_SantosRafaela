from pyscript import document

def average_finder(event):
    # Get the two numbers (default to 0 if empty)
    num1 = float(document.getElementById("input1").value or 0)
    num2 = float(document.getElementById("input2").value or 0)

    # Compute average
    avg = (num1 + num2) / 2

    # Decide if passed or failed
    result = "✅ Passed" if avg >= 75 else "❌ Failed"

    # Show result
    document.getElementById("output").innerHTML = f"Average: {avg:.1f} <br>{result}"
