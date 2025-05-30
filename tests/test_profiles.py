from scripts.budget_allocate import allocate_budget 
from scripts.generate_advice import generate_advice
from scripts.get_benchmark import get_benchmark
from scripts.compare_with_ideal import compare_with_ideal



test_profiles = [
    {"income": 1500, "expenses": 1200},
    {"income": 4000, "expenses": 2500},
    {"income": 8000, "expenses": 6000},
    {"income": 15000, "expenses": 8000},
]

for profile in test_profiles:
    allocations = allocate_budget(profile["income"])
    advice = generate_advice(profile["income"], profile["expenses"], allocations)
    benchmark = get_benchmark(profile["income"])
    comparison = compare_with_ideal(profile["income"], allocations)
    print(f"\nProfile: Income=${profile['income']}, Expenses=${profile['expenses']}")
    print("Allocations:", allocations)
    print("Advice:", advice)
    print("Benchmark:", benchmark)
    print("Comparison with Ideal:", comparison)
