"""
database.py
Contains functions and structures for managing predefined materials,
file storage (JSON/CSV), path management (pathlib), and simulated data generation (random).
Part of Task 6: System Integration
"""

import csv
import json
import random
from pathlib import Path
from typing import List, Optional

from .material import Material, Metal, Plastic, Composite
from .properties import MaterialProperties
from .tests import StressStrainTest, TestRecord


# Default directory for persistent data and exports
DEFAULT_DATA_DIR = Path("data")


# ==============================================================================
# PREDEFINED MATERIALS DATABASE
# ==============================================================================
def get_default_materials() -> List[Material]:
    """Returns the baseline library of pre-configured engineering materials."""
    return [
        Metal("Steel", yield_strength=250.0, elastic_modulus=200.0, description="Structural carbon steel"),
        Metal("Aluminum", yield_strength=95.0, elastic_modulus=69.0, description="General structural aluminum alloy"),
        Metal("Titanium", yield_strength=880.0, elastic_modulus=114.0, description="High-performance aerospace titanium"),
        Plastic("ABS Polymer", yield_strength=45.0, elastic_modulus=2.5, description="Engineering thermoplastic"),
        Composite("Carbon Fiber", yield_strength=500.0, elastic_modulus=120.0, description="High-strength woven carbon composite"),
    ]


class MaterialDatabase:
    """Manages the catalog of predefined and custom materials."""

    def __init__(self):
        self._materials: List[Material] = get_default_materials()

    @property
    def materials(self) -> List[Material]:
        """Returns the list of currently registered materials."""
        return self._materials

    def add_material(self, material: Material) -> None:
        """Registers a new custom material into the database."""
        self._materials.append(material)

    def find_by_name(self, name: str) -> Optional[Material]:
        """Searches for a material by name (case-insensitive)."""
        for m in self._materials:
            if m.name.lower() == name.lower():
                return m
        return None


# ==============================================================================
# STANDARD LIBRARY: PATHLIB & DIRECTORY MANAGEMENT
# ==============================================================================
def ensure_data_directory(directory: Path = DEFAULT_DATA_DIR) -> Path:
    """Ensures that the target directory exists, creating parent folders if necessary."""
    directory.mkdir(parents=True, exist_ok=True)
    return directory


# ==============================================================================
# STANDARD LIBRARY: JSON (SAVING & LOADING SESSIONS)
# ==============================================================================
def save_session_to_json(records: List[TestRecord], filename: str = "session_history.json", directory: Path = DEFAULT_DATA_DIR) -> Path:
    """
    Saves a collection of test records to a JSON file.
    """
    ensure_data_directory(directory)
    filepath = directory / filename

    data = [record.to_dict() for record in records]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return filepath


def load_session_from_json(filename: str = "session_history.json", directory: Path = DEFAULT_DATA_DIR) -> List[TestRecord]:
    """
    Loads test records from a previously saved JSON file.
    """
    filepath = directory / filename
    if not filepath.exists():
        raise FileNotFoundError(f"History file not found at: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [TestRecord.from_dict(item) for item in data]


# ==============================================================================
# STANDARD LIBRARY: CSV (EXPORTING TEST DATA)
# ==============================================================================
def export_session_to_csv(records: List[TestRecord], filename: str = "test_export.csv", directory: Path = DEFAULT_DATA_DIR) -> Path:
    """
    Exports test records into a standardized CSV spreadsheet format.
    """
    ensure_data_directory(directory)
    filepath = directory / filename

    fieldnames = [
        "timestamp", "material", "category", "force", "area", "original_length",
        "change_in_length", "stress_pa", "stress_mpa", "strain",
        "rated_modulus_gpa", "calculated_modulus_gpa", "yield_strength_mpa",
        "fos", "safety_status"
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record.to_dict())

    return filepath


# ==============================================================================
# STANDARD LIBRARY: RANDOM (SIMULATED TEST DATA GENERATOR)
# ==============================================================================
def generate_simulated_test(target_safety: str = "random") -> StressStrainTest:
    """
    Generates realistic, randomized engineering test parameters for simulation.
    
    Args:
        target_safety: 'safe', 'caution', 'unsafe', or 'random'
    """
    # Random realistic original length between 0.5m and 12.0m
    original_length = round(random.uniform(0.5, 10.0), 2)

    # Random realistic cross-sectional area between 0.001 m^2 and 0.05 m^2
    area = round(random.uniform(0.002, 0.025), 6)

    # Random force between 5,000 N and 120,000 N
    force = round(random.uniform(5000.0, 100000.0), 2)

    # Calculate resulting stress in Pa
    stress_pa = force / area

    # Choose a simulated modulus between 50 GPa and 220 GPa to estimate plausible strain
    assumed_e_pa = random.uniform(60.0, 200.0) * 1e9
    plausible_strain = stress_pa / assumed_e_pa

    # Change in length based on strain
    change_in_length = round(plausible_strain * original_length, 6)

    return StressStrainTest(
        force=force,
        area=area,
        original_length=original_length,
        change_in_length=change_in_length
    )

