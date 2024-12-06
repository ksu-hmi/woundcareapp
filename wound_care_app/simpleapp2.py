def dressing_instructions(stage):
    """
    Provide dressing instructions based on the wound stage.
    """
    instructions = {
        "1": (
            "Stage 1: Non-blanchable erythema of intact skin.\n"
            "Instructions:\n"
            "- Keep the skin clean and dry.\n"
            "- Apply a moisture barrier cream or protective dressing (e.g., transparent film).\n"
            "- Relieve pressure on the affected area and avoid friction."
        ),
        "2": (
            "Stage 2: Partial-thickness skin loss with exposed dermis.\n"
            "Instructions:\n"
            "- Clean the wound with saline or an appropriate wound cleanser.\n"
            "- Apply a moisture-retentive dressing, such as hydrocolloid or foam dressing.\n"
            "- Protect the wound from further pressure and contamination."
        ),
        "3": (
            "Stage 3: Full-thickness skin loss involving subcutaneous tissue but not bone, tendon, or muscle.\n"
            "Instructions:\n"
            "- Clean the wound with saline or an appropriate wound cleanser.\n"
            "- Debride necrotic tissue if present (consult a healthcare professional).\n"
            "- Apply a dressing that promotes moisture balance, such as hydrocolloid, foam, or alginate.\n"
            "- Consider additional measures to reduce bacterial load, such as antimicrobial dressings."
        ),
        "4": (
            "Stage 4: Full-thickness skin and tissue loss with exposed bone, tendon, or muscle.\n"
            "Instructions:\n"
            "- Clean the wound with saline or an appropriate wound cleanser.\n"
            "- Debride necrotic tissue (consult a healthcare professional).\n"
            "- Use advanced wound dressings such as alginate or foam, and consider negative pressure wound therapy (NPWT).\n"
            "- Ensure comprehensive wound care management with consultation from a wound care specialist."
        ),
        "unstageable": (
            "Unstageable: Obscured full-thickness skin and tissue loss.\n"
            "Instructions:\n"
            "- Consult a healthcare professional for debridement of eschar or slough.\n"
            "- Once the wound bed is visible, reassess for proper staging and care.\n"
            "- Apply a moist wound dressing, such as hydrogel or foam, to support healing."
        ),
        "deep tissue injury": (
            "Deep Tissue Injury: Persistent non-blanchable deep red, maroon, or purple discoloration.\n"
            "Instructions:\n"
            "- Avoid further pressure or trauma to the area.\n"
            "- Use protective dressings, such as foam or hydrocolloid, to cushion and protect the area.\n"
            "- Monitor closely for progression or worsening of the wound."
        ),
    }
    return instructions.get(stage.lower(), "Unknown stage. Please consult a healthcare professional.")

def main():
    print("Welcome to the Wound Care Dressing Instructions App!")
    print("Type the stage of the wound (e.g., '1', '2', '3', '4', 'unstageable', or 'deep tissue injury'), and get wound care instructions.")
    
    while True:
        stage = input("\nEnter the wound stage (or type 'exit' to quit): ").strip()
        if stage.lower() == 'exit':
            print("Thank you for using the Wound Care Dressing Instructions App. Goodbye!")
            break
        
        instructions = dressing_instructions(stage)
        print(f"\n{instructions}")

if __name__ == "__main__":
    main()
