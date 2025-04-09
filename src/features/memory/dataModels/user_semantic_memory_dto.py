from typing import Dict, List, Literal, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime

class Fact(BaseModel):
    """
    A fact extracted from the conversation.
    """
    fact: str = Field(description="The fact about the user, can be about the user, proferences, new facts about the world, etc.")
    context: str = Field(description="The context of the fact, ex: 'during the user introduction', 'user complaining about the weather', 'user talking about their family', etc.")

class DefaultSemanticMemoryDataModel(BaseModel):
    """
    Data model for maintaining up-to-date information obtained from the conversation.
    """
    facts: List[Fact] = Field(description="A list of facts extracted from the conversation")
    
    class Config:
        json_schema_extra = {
            "name": "Facts",
            "description": "Update this document to maintain up-to-date information about the user in the conversation.",
            "update_mode": "patch"
        }
    
    @staticmethod
    def get_model_name() -> str:
        """Returns the model name as defined in the schema."""
        return DefaultSemanticMemoryDataModel.model_config["json_schema_extra"]["name"]
    
    @staticmethod
    def get_class_name() -> str:
        """Returns the class name of the model."""
        return DefaultSemanticMemoryDataModel.__name__
    
    @staticmethod
    def get_schema() -> Dict:
        """Returns the complete JSON schema of the model."""
        return DefaultSemanticMemoryDataModel.model_json_schema()
    
    @staticmethod
    def get_schema_by_mode(mode: str = "all") -> Dict:
        """
        Returns the schema in different modes:
        - 'all': Complete schema with all properties
        - 'required': Only required fields
        - 'optional': Only optional fields
        - 'descriptions': Only field descriptions
        """
        schema = DefaultSemanticMemoryDataModel.model_json_schema()
        
        if mode == "required":
            return {k: v for k, v in schema["properties"].items() if k in schema.get("required", [])}
        elif mode == "optional":
            return {k: v for k, v in schema["properties"].items() if k not in schema.get("required", [])}
        elif mode == "descriptions":
            return {k: v.get("description", "") for k, v in schema["properties"].items()}
        else:
            return schema

class UserProfileDataModel(BaseModel):
    """
    Data model for maintaining up-to-date information about the user in the conversation.
    """
    user_name: str = Field(description="The user's preferred name")
    age: int = Field(description="The user's age")
    interests: List[str] = Field(description="A list of the user's interests")
    home: str = Field(description="Description of the user's home town/neighborhood")
    occupation: str = Field(description="The user's current occupation or profession")
    conversation_preferences: List[str] = Field(description="A list of the user's preferred conversation styles, pronouns, topics they want to avoid, preferred format for receiving information (text, audio, visual), etc.")
    accessibility_preferences: List[str] = Field(description="A list of the user's preferred accessibility preferences")
    preferred_language: str = Field(default="pt-BR", description="The user's preferred language for communication")
    
    class Config:
        json_schema_extra = {
            "name": "UserProfile",
            "description": "Update this document to maintain up-to-date information about the user in the conversation.",
            "update_mode": "patch"
        }
    
    @staticmethod
    def get_model_name() -> str:
        """Returns the model name as defined in the schema."""
        return UserProfileDataModel.model_config["json_schema_extra"]["name"]
    
    @staticmethod
    def get_class_name() -> str:
        """Returns the class name of the model."""
        return UserProfileDataModel.__name__
    
    @staticmethod
    def get_schema() -> Dict:
        """Returns the complete JSON schema of the model."""
        return UserProfileDataModel.model_json_schema()
    
    @staticmethod
    def get_schema_by_mode(mode: str = "all") -> Dict:
        """
        Returns the schema in different modes:
        - 'all': Complete schema with all properties
        - 'required': Only required fields
        - 'optional': Only optional fields
        - 'descriptions': Only field descriptions
        """
        schema = UserProfileDataModel.model_json_schema()
        
        if mode == "required":
            return {k: v for k, v in schema["properties"].items() if k in schema.get("required", [])}
        elif mode == "optional":
            return {k: v for k, v in schema["properties"].items() if k not in schema.get("required", [])}
        elif mode == "descriptions":
            return {k: v.get("description", "") for k, v in schema["properties"].items()}
        else:
            return schema

class ComplexUserProfileDataModel(BaseModel):
    """
    Data model for maintaining up-to-date information about the user in the conversation.
    """
    # Basic Information
    user_name: str = Field(description="The user's preferred name")
    age: int = Field(description="The user's age")
    interests: List[str] = Field(description="A list of the user's interests")
    home: str = Field(description="Description of the user's home town/neighborhood")
    
    # Additional Personal Information
    preferred_language: str = Field(default="pt-BR", description="The user's preferred language for communication")
    secondary_languages: List[str] = Field(default=[], description="List of other languages the user knows or can communicate in")
    education_level: Optional[str] = Field(default=None, description="The user's highest level of education completed")
    technical_background: Optional[str] = Field(default=None, description="Description of the user's technical knowledge and expertise")
    
    # Communication Preferences
    communication_style: str = Field(default="formal", description="User's preferred communication style (formal, casual, technical, etc.)")
    preferred_pronouns: Optional[str] = Field(default=None, description="The user's preferred pronouns for addressing them")
    topics_to_avoid: List[str] = Field(default=[], description="List of topics or subjects the user prefers to avoid in conversations")
    preferred_response_length: str = Field(default="medium", description="User's preferred length for responses (short, medium, detailed)")
    
    # Professional Context
    industry: Optional[str] = Field(default=None, description="The industry or sector the user works in")
    work_environment: Optional[str] = Field(default=None, description="Description of the user's work environment and context")
    professional_goals: List[str] = Field(default=[], description="List of the user's professional objectives and career goals")
    
    # Learning Preferences
    learning_style: Optional[str] = Field(default=None, description="User's preferred learning style (visual, auditory, reading/writing, kinesthetic)")
    preferred_explanation_depth: str = Field(default="balanced", description="User's preferred level of explanation detail (basic, balanced, advanced)")
    
    # Interaction History
    interaction_frequency: str = Field(default="regular", description="How often the user intends to interact with the assistant (occasional, regular, frequent)")
    preferred_interaction_times: List[str] = Field(default=[], description="List of preferred times or periods for interaction")
    
    # Accessibility Preferences
    accessibility_needs: List[str] = Field(default=[], description="List of any accessibility requirements or accommodations needed")
    preferred_output_format: str = Field(default="text", description="User's preferred format for receiving information (text, audio, visual)")
    
    # Cultural Context
    cultural_background: Optional[str] = Field(default=None, description="User's cultural background and context")
    
    # System Preferences
    #preferred_ai_personality: str = Field(default="professional", description="User's preferred AI assistant personality (professional, friendly, technical, etc.)")
    #notification_preferences: List[str] = Field(default=[], description="List of user's preferences regarding system notifications and alerts")
    
    class Config:
        json_schema_extra = {
            "name": "ComplexUserProfile",
            "description": "Update this document to maintain up-to-date information about the user in the conversation.",
            "update_mode": "patch"
        }
    
    @staticmethod
    def get_model_name() -> str:
        """Returns the model name as defined in the schema."""
        return ComplexUserProfileDataModel.model_config["json_schema_extra"]["name"]
    
    @staticmethod
    def get_class_name() -> str:
        """Returns the class name of the model."""
        return ComplexUserProfileDataModel.__name__
    
    @staticmethod
    def get_schema() -> Dict:
        """Returns the complete JSON schema of the model."""
        return ComplexUserProfileDataModel.model_json_schema()
    
    @staticmethod
    def get_schema_by_mode(mode: str = "all") -> Dict:
        """
        Returns the schema in different modes:
        - 'all': Complete schema with all properties
        - 'required': Only required fields
        - 'optional': Only optional fields
        - 'descriptions': Only field descriptions
        """
        schema = ComplexUserProfileDataModel.model_json_schema()
        
        if mode == "required":
            return {k: v for k, v in schema["properties"].items() if k in schema.get("required", [])}
        elif mode == "optional":
            return {k: v for k, v in schema["properties"].items() if k not in schema.get("required", [])}
        elif mode == "descriptions":
            return {k: v.get("description", "") for k, v in schema["properties"].items()}
        else:
            return schema 