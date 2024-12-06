def stage_wound(characteristics):
    """
    Determine the stage of the wound based on its characteristics.
    """
    characteristics = characteristics.lower().strip()
    
    if "intact skin" in characteristics and "redness" in characteristics:
        return "Stage 1: Non-blanchable erythema of intact skin."
    elif "partial thickness" in characteristics and ("blister" in characteristics or "shallow ulcer" in characteristics):
        return "Stage 2: Partial-thickness skin loss with exposed dermis."
    elif "full thickness" in characteristics and "subcutaneous fat" in characteristics:
        return "Stage 3: Full-thickness skin loss involving subcutaneous tissue but not bone, tendon, or muscle."
    elif "full thickness" in characteristics and ("bone" in characteristics or "tendon" in characteristics or "muscle" in characteristics):
        return "Stage 4: Full-thickness skin and tissue loss with exposed bone, tendon, or muscle."
    elif "eschar" in characteristics or "slough" in characteristics:
        return "Unstageable: Obscured full-thickness skin and tissue loss."
    elif "deep tissue" in characteristics and ("discolored skin" in characteristics or "blood-filled blister" in characteristics):
        return "Deep Tissue Injury: Persistent non-blanchable deep red, maroon, or purple discoloration."
    else:
        return "Unknown stage"

def dressing_instructions(stage):
    """
    Provide dressing instructions based on the wound stage.
    """
    instructions = {
        "Stage 1": (
            "Keep the skin clean and dry.\n"
            "Apply a moisture barrier cream or protective dressing (e.g., transparent film).\n"
            "Relieve pressure on the affected area and avoid friction."
        ),
        "Stage 2": (
            "Clean the wound with saline or an appropriate wound cleanser.\n"
            "Apply a moisture-retentive dressing, such as hydrocolloid or foam dressing.\n"
            "Protect the wound from further pressure and contamination."
        ),
        "Stage 3": (
            "Clean the wound with saline or an appropriate wound cleanser.\n"
            "Debride necrotic tissue if present (consult a healthcare professional).\n"
            "Apply a dressing that promotes moisture balance, such as hydrocolloid, foam, or alginate.\n"
            "Consider additional measures to reduce bacterial load, such as antimicrobial dressings."
        ),
        "Stage 4": (
            "Clean the wound with saline or an appropriate wound cleanser.\n"
            "Debride necrotic tissue (consult a healthcare professional).\n"
            "Use advanced wound dressings such as alginate or foam, and consider negative pressure wound therapy (NPWT).\n"
            "Ensure comprehensive wound care management with consultation from a wound care specialist."
        ),
        "Unstageable": (
            "Consult a healthcare professional for debridement of eschar or slough.\n"
            "Once the wound bed is visible, reassess for proper staging and care.\n"
            "Apply a moist wound dressing, such as hydrogel or foam, to support healing."
        ),
        "Deep Tissue Injury": (
            "Avoid further pressure or trauma to the area.\n"
            "Use protective dressings, such as foam or hydrocolloid, to cushion and protect the area.\n"
            "Monitor closely for progression or worsening of the wound."
        ),
        "Unknown stage": "Unable to provide dressing instructions. Please consult a healthcare professional."
    }
    return instructions.get(stage.split(":")[0], "No instructions available.")

def main():
    print("Welcome to the Wound Care Staging and Dressing Instructions App!")
    print("Type in the characteristics of the wound, and the app will stage it and provide dressing recommendations.")
    print("For example: 'intact skin with redness' or 'full thickness with exposed bone'.")
    
    while True:
        user_input = input("\nEnter wound characteristics (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Wound Care App. Goodbye!")
            break
        
        stage = stage_wound(user_input)
        print(f"\n{stage}")
        
        if stage != "Unknown stage":
            instructions = dressing_instructions(stage)
            print("\nRecommended Wound Care Dressing:")
            print(instructions)

if __name__ == "__main__":
    main()


