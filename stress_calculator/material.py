"""
material.py
Contains the Material class hierarchy and subclasses.
Part of Task 6: System Integration
"""

from typing import Dict, Any
from .properties import MaterialProperties


class Material:
    """
    Base class modeling an engineering material, its mechanical properties,
    and string representation.
    """

    def __init__(self, name: str, properties: MaterialProperties):
        self.name: str = name
        self.properties: MaterialProperties = properties

    @property
    def yield_strength(self) -> float:
        """Rated Yield Strength in MPa."""
        return self.properties.yield_strength

    @property
    def elastic_modulus(self) -> float:
        """Rated Young's Modulus in GPa."""
        return self.properties.elastic_modulus

    @property
    def category(self) -> str:
        """Category type (e.g. Metal, Plastic, Composite)."""
        return self.properties.category

    def to_dict(self) -> Dict[str, Any]:
        """Serializes material to dictionary format."""
        return {
            "name": self.name,
            "yield_strength_mpa": self.yield_strength,
            "elastic_modulus_gpa": self.elastic_modulus,
            "category": self.category,
            "description": self.properties.description
        }

    def __str__(self) -> str:
        return f"{self.name} [{self.category}] (Yield Strength: {self.yield_strength:.1f} MPa, Young's Modulus: {self.elastic_modulus:.1f} GPa)"

    def __eq__(self, other: object) -> bool:
        """Two materials are equal if their name and properties match."""
        if not isinstance(other, Material):
            return NotImplemented
        return self.name == other.name and self.properties == other.properties

    def __lt__(self, other: "Material") -> bool:
        """Materials compare by yield strength, allowing them to be sorted."""
        if not isinstance(other, Material):
            return NotImplemented
        return self.yield_strength < other.yield_strength

    def __gt__(self, other: "Material") -> bool:
        if not isinstance(other, Material):
            return NotImplemented
        return self.yield_strength > other.yield_strength

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Material":
        """Reconstructs a Material from a dictionary produced by to_dict()."""
        props = MaterialProperties(
            yield_strength=data["yield_strength_mpa"],
            elastic_modulus=data["elastic_modulus_gpa"],
            category=data.get("category", "Metal"),
            description=data.get("description")
        )
        return cls(name=data["name"], properties=props)


class Metal(Material):
    """Subclass representing metallic alloys."""
    def __init__(self, name: str = "Structural Steel", yield_strength: float = 250.0, elastic_modulus: float = 200.0, description: str = "Common structural alloy"):
        super().__init__(name, MaterialProperties(yield_strength, elastic_modulus, category="Metal", description=description))


class Plastic(Material):
    """Subclass representing polymers and plastics."""
    def __init__(self, name: str = "ABS Polymer", yield_strength: float = 45.0, elastic_modulus: float = 2.5, description: str = "Thermoplastic polymer"):
        super().__init__(name, MaterialProperties(yield_strength, elastic_modulus, category="Plastic", description=description))


class Composite(Material):
    """Subclass representing composite materials."""
    def __init__(self, name: str = "Carbon Fiber Composite", yield_strength: float = 500.0, elastic_modulus: float = 120.0, description: str = "High-strength fiber composite"):
        super().__init__(name, MaterialProperties(yield_strength, elastic_modulus, category="Composite", description=description))

