from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# ------------------ Ceaser Cypher Function ----------------------------
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(start_text, shift_amount, cipher_direction):
    shift_amount %= 26
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    return end_text


# -------------------- Flask routes -------------------------------
@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        message = request.form.get('message_text', False)
        shift_number = int(request.form.get('shift_number', False))
        if shift_number < 0:
            shift_number *= -1
        cypher_direction = request.form.get('option', False)
        output = ceaser(message, shift_number, cypher_direction)
        print(output)
        return render_template('index.html', direction=cypher_direction, endtext=output, show_div=True)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
