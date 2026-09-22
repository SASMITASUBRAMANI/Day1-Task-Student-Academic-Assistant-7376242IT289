"""Tools available to the AI agent."""
import ast
import operator
from config import ATTENDANCE, ASSIGNMENTS

def get_attendance(subject: str) -> str:
    value = ATTENDANCE.get(subject.strip().upper())
    return f"{value}%" if value is not None else f"Unknown subject: {subject}"

def get_pending_assignments() -> str:
    pending = [
        f"{subject} ({info['due_days']} days)"
        for subject, info in ASSIGNMENTS.items()
        if info["status"] == "pending"
    ]
    return ", ".join(pending) if pending else "No pending assignments."

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}

def _evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_evaluate(node.left), _evaluate(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_evaluate(node.operand))
    raise ValueError("Unsupported expression")

def calculator(expression: str) -> str:
    try:
        return str(_evaluate(ast.parse(expression, mode="eval").body))
    except Exception as error:
        return f"Calculator error: {error}"

TOOL_FUNCTIONS = {
    "get_attendance": get_attendance,
    "get_pending_assignments": get_pending_assignments,
    "calculator": calculator,
}

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_attendance",
            "description": "Get attendance percentage for DBMS, AI, or CN.",
            "parameters": {
                "type": "object",
                "properties": {"subject": {"type": "string"}},
                "required": ["subject"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_pending_assignments",
            "description": "Get the student's pending assignments and days remaining.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate basic arithmetic using + - * / and brackets.",
            "parameters": {
                "type": "object",
                "properties": {"expression": {"type": "string"}},
                "required": ["expression"],
            },
        },
    },
]
