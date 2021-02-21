from typing import Any

def success(data: Any, **kwargs) -> dict:
    return {
        **{ 
            'status': True, 
            'result': data
        }, 
        **kwargs
    }, 200

def error(code: int=500, message: str='Internal server error.', **kwargs) -> dict:
    return {
        **{ 
            'status': False, 
            'message': message, 
        }, 
        **kwargs
    }, (code if isinstance(code, int) else 500)