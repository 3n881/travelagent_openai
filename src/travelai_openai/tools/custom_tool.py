from crewai.tools import BaseTool
from typing import Type, Dict, Union, List
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

class BookingLinksInput(BaseModel):
    """Input schema for BookingLinksTool."""
    service_type: str = Field(
        ..., 
        description="Type of service to get booking links for (e.g., 'flights', 'hotels', 'activities', 'transfers')"
    )

class BookingLinksTool(BaseTool):
    name: str = "Booking Links Tool"
    description: str = (
        "A tool for accessing various booking service links for flights, hotels, "
        "activities, and transfers. Returns booking URLs for the requested service type."
    )
    args_schema: Type[BaseModel] = BookingLinksInput
    links: Dict[str, Union[str, List[str]]] = Field(
        default_factory=dict,
        description="Dictionary of booking service links"
    )

    class Config:
        arbitrary_types_allowed = True

    def _run(self, service_type: str) -> str:
        """Returns the booking link for the requested service type"""
        if service_type not in self.links:
            available_services = ', '.join(self.links.keys())
            return f"Link not found for service type: {service_type}. Available services: {available_services}"
        return str(self.links[service_type])

    @classmethod
    def create(cls, links: Dict[str, Union[str, List[str]]]) -> 'BookingLinksTool':
        """Factory method to create a BookingLinksTool instance"""
        instance = cls()
        instance.links = links
        return instance
