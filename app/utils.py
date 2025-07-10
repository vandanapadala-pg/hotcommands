from app.schemas import Parameter
from typing import List, Dict, Any

def substitute_parameters(query_text: str, parameters: List[Parameter], values: Dict[str, Any]) -> str:
    for param in parameters:
        val = values.get(param.name, param.default)
        if val is None and param.required:
            raise ValueError(f"Missing required parameter: {param.name}")
        query_text = query_text.replace(f"{{{{{param.name}}}}}", str(val))
    return query_text
