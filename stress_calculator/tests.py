"""
tests.py
Contains classes related to stress-strain tests, evaluation logic, and test collections.
Part of Task 6: System Integration
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Tuple, Optional, Set
from .material import Material
from .utils import (
    calculate_stress_pa,
    calculate_stress_mpa,
    calculate_strain,
    calculate_youngs_modulus_gpa,
    calculate_factor_of_safety,
    determine_safety_status,
    display_header,
    BANNER_WIDTH,
    UNITS,
)


@dataclass
class StressStrainTest:
    """
    Encapsulates the physical measurements of a tension or compression test.
    Incorporates standard library datetime for test timestamping.
    """
    force: float            # Applied Force in Newtons (N)
    area: float             # Cross-Sectional Area in square meters (m^2)
    original_length: float  # Original Length in meters (m)
    change_in_length: float # Change in Length in meters (m)
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


@dataclass
class TestRecord:
    """
    Complete evaluation record for a physical test performed on a specific material.
    """
    material: str
    category: str
    force: float
    area: float
    original_length: float
    change_in_length: float
    stress_pa: float
    stress_mpa: float
    strain: float
    rated_modulus_gpa: float
    calculated_modulus_gpa: float
    yield_strength_mpa: float
    fos: float
    safety_status: str
    timestamp: str

    def to_dict(self) -> Dict[str, Any]:
        """Converts the record into a dictionary for JSON/CSV serialization."""
        return {
            "timestamp": self.timestamp,
            "material": self.material,
            "category": self.category,
            "force": self.force,
            "area": self.area,
            "original_length": self.original_length,
            "change_in_length": self.change_in_length,
            "stress_pa": self.stress_pa,
            "stress_mpa": self.stress_mpa,
            "strain": self.strain,
            "rated_modulus_gpa": self.rated_modulus_gpa,
            "calculated_modulus_gpa": self.calculated_modulus_gpa,
            "yield_strength_mpa": self.yield_strength_mpa,
            "fos": self.fos,
            "safety_status": self.safety_status
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "TestRecord":
        """Recreates a TestRecord instance from a dictionary."""
        return cls(
            material=d["material"],
            category=d.get("category", "General"),
            force=float(d["force"]),
            area=float(d["area"]),
            original_length=float(d["original_length"]),
            change_in_length=float(d["change_in_length"]),
            stress_pa=float(d["stress_pa"]),
            stress_mpa=float(d["stress_mpa"]),
            strain=float(d["strain"]),
            rated_modulus_gpa=float(d["rated_modulus_gpa"]),
            calculated_modulus_gpa=float(d["calculated_modulus_gpa"]),
            yield_strength_mpa=float(d["yield_strength_mpa"]),
            fos=float(d["fos"]),
            safety_status=d["safety_status"],
            timestamp=d.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )


def evaluate_test_on_material(material: Material, test: StressStrainTest) -> TestRecord:
    """
    Computes all mechanical response values for a material given the physical test parameters.
    """
    stress_pa = calculate_stress_pa(test.force, test.area)
    stress_mpa = calculate_stress_mpa(stress_pa)
    strain = calculate_strain(test.change_in_length, test.original_length)
    calc_modulus = calculate_youngs_modulus_gpa(stress_pa, strain)
    fos = calculate_factor_of_safety(material.yield_strength, stress_mpa)
    status = determine_safety_status(fos)

    return TestRecord(
        material=material.name,
        category=material.category,
        force=test.force,
        area=test.area,
        original_length=test.original_length,
        change_in_length=test.change_in_length,
        stress_pa=stress_pa,
        stress_mpa=stress_mpa,
        strain=strain,
        rated_modulus_gpa=material.elastic_modulus,
        calculated_modulus_gpa=calc_modulus,
        yield_strength_mpa=material.yield_strength,
        fos=fos,
        safety_status=status,
        timestamp=test.timestamp
    )


def display_test_record(record: TestRecord, units: Tuple[str, ...] = UNITS) -> None:
    """Formats and prints a single completed test record with precision."""
    display_header("Calculation Results")

    print(f"Timestamp:                {record.timestamp}")
    print("Material Info:")
    print(f" - Material Selected:     {record.material} [{record.category}]")
    print(f" - Yield Strength:        {record.yield_strength_mpa:,.2f} {units[3]}")
    print(f" - Rated Young's Modulus: {record.rated_modulus_gpa:,.2f} {units[4]}")
    print(" - " * 20)

    print("Input Parameters:")
    print(f" - Applied Force:         {record.force:,.2f} {units[0]}")
    print(f" - Cross Sectional Area:  {record.area:.6f} {units[1]}")
    print(f" - Original Length:       {record.original_length:.4f} {units[2]}")
    print(f" - Change in Length:      {record.change_in_length:.6f} {units[2]}")
    print(" - " * 20)

    print("Calculated Outputs:")
    print(f" - Engineering Stress:    {record.stress_mpa:,.2f} {units[3]} ({record.stress_pa:,.2f} Pa)")
    print(f" - Engineering Strain:    {record.strain:.6f}")
    print(f" - Calc. Young's Modulus: {record.calculated_modulus_gpa:,.2f} {units[4]}")
    print(" - " * 20)

    print("Safety Analysis:")
    print(f" - Factor of Safety:      {record.fos:.2f}")
    print(f" - Safety Status:         {record.safety_status}")
    print("=" * BANNER_WIDTH)




        return {
            "total": total,
            "unique_materials": sorted(list(self.unique_materials)),
            "safe_count": safe_count,
            "max_stress": max(stress_vals),
            "min_stress": min(stress_vals),
            "avg_stress": sum(stress_vals) / total
        }

    def display_summary_report(self) -> None:
        """Displays the Session Summary Report."""
        display_header("SESSION SUMMARY REPORT")

        stats = self.compute_statistics()
        if stats is None:
            print("No calculations were performed during this session.")
            return

        print(f"Total Calculations Performed: {stats['total']}")
        print(f"Unique Materials Tested:      {', '.join(stats['unique_materials'])}")
        print(f"Total Safe Tests:             {stats['safe_count']} out of {stats['total']}")
        print(" - " * 20)
        print("STRESS STATISTICS:")
        print(f" - Highest Stress Recorded:   {stats['max_stress']:,.2f} {UNITS[3]}")
        print(f" - Lowest Stress Recorded:    {stats['min_stress']:,.2f} {UNITS[3]}")
        print(f" - Average Stress Across:     {stats['avg_stress']:,.2f} {UNITS[3]}")
        print("=" * BANNER_WIDTH)

