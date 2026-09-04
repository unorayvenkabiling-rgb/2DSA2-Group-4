"""
properties.py
Contains data-oriented material properties and appropriate dataclasses.
Part of Task 6: System Integration
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class MaterialProperties:
    """
    Data-oriented model for physical and mechanical properties of materials.
    
    Attributes:
        yield_strength: Yield strength in Megapascals (MPa)
        elastic_modulus: Young's Modulus of elasticity in Gigapascals (GPa)
        category: Material class category (Metal, Plastic, Composite, etc.)
        description: Optional notes regarding the material grade
    """
    yield_strength: float
    elastic_modulus: float
    category: str = "Metal"
    description: Optional[str] = None

    def __post_init__(self):
        if self.yield_strength <= 0:
            raise ValueError("Yield strength must be strictly greater than zero.")
        if self.elastic_modulus <= 0:
            raise ValueError("Elastic modulus must be strictly greater than zero.")

