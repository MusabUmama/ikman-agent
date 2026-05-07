from typing import Any


class IkmanAgentError(Exception):
    def __init__(self, message: str, details: Any = None) -> None:
        super().__init__(message)
        self.details = details


class LLMError(IkmanAgentError):
    pass


class ToolError(IkmanAgentError):
    def __init__(self, tool_name: str, message: str, details: Any = None) -> None:
        super().__init__(message, details=details)
        self.tool_name = tool_name


class ScrapingError(ToolError):
    pass


class WhatsAppError(ToolError):
    pass


class AgentError(IkmanAgentError):
    def __init__(self, agent_name: str, message: str, details: Any = None) -> None:
        super().__init__(message, details=details)
        self.agent_name = agent_name


class ConversationError(AgentError):
    def __init__(
        self,
        agent_name: str,
        phase: str,
        message: str,
        details: Any = None,
    ) -> None:
        super().__init__(agent_name=agent_name, message=message, details=details)
        self.phase = phase


class ConfigurationError(IkmanAgentError):
    pass
