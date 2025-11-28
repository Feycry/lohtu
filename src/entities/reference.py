from entities.all_fields import ORDERED_KEYS


class Reference:

    def __init__(self, reference_id, **fields):
        self.id = reference_id
        for key, value in fields.items():
            setattr(self, key, value)

    def __getitem__(self, key):

        return getattr(self, key, None)

    def __str__(self):
        parts = []
        for key in ORDERED_KEYS:
            value = getattr(self, key, None)
            if value:
                label = key.replace("_", " ").title()
                if key == "ref_type":
                    parts.append(f"Type: @{value}")
                else:
                    parts.append(f"{label}: {value}")
        return ", ".join(parts) if parts else f"Reference #{self.id}"

    def to_bibtex(self):
        parts = []
        for key in ORDERED_KEYS:
            value = getattr(self, key, None)
            if value:
                if key == "ref_type":
                    parts.append(f"@{value}" + "{" + f"{getattr(self, "id")}")
                else:
                    parts.append(f"{key} = " + "{" + f"{value}" + "}")
        return ",\n\t".join(parts) + "\n}" if parts else f"ERROR: Reference #{self.id}"
