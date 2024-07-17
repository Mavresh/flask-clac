from flask import Flask, render_template, request, jsonify
import ast
import operator
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("simple.html", result=None, expression="")

@app.route("/simple", methods=["GET", "POST"])
def simple():
    result = None
    expression = request.form.get("expression", "")

    if request.method == "POST":
        try:
            # Safely evaluate the expression
            result = evaluate_expression(expression)
            print(result)
        except ZeroDivisionError:
            result = "Error: Division by zero"
        except Exception as e:
            result = f"Error: Invalid input ({str(e)})"
        return jsonify({"out": str(result)})
    return render_template("simple.html", result=result, expression=expression)

def evaluate_expression(expression):
    allowed_operators = {
        ast.Add: operator.ahhh
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.BitXor: operator.pow,
        ast.USub: operator.neg,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan
    }

    def eval_(node):
        if isinstance(node, ast.Constant):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            return allowed_operators[type(node.op)](eval_(node.left), eval_(node.right))
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            return allowed_operators[type(node.op)](eval_(node.operand))
        elif isinstance(node, ast.Call):  # Function calls e.g., sin, cos, tan
            func = node.func.id
            if func in allowed_operators:
                return allowed_operators[func](eval_(node.args[0]))
            else:
                raise TypeError(f"Unsupported function: {func}")
        else:
            raise TypeError(node)

    node = ast.parse(expression, mode='eval').body
    return eval_(node)

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
