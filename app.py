
import streamlit as st

def main():
    st.title("Simple Calculator")

    # Input fields
    num1 = st.number_input("Enter the first number:", format="%.2f")
    num2 = st.number_input("Enter the second number:", format="%.2f")

    # Select operation
    operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

    # Calculate result
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."

        st.write(f"Result: {result}")

if __name__ == "__main__":
    main()
