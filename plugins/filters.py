def keyword(terms: dict = {}, msg: str = ""):
    for k, m in terms.items():
        if k in msg:
            return m


def build_shared_info(mentioned: dict = {}) -> str:
    """Colecta todo lo que hay en el slot `mentioned` y lo devuelve como un
    texto plano, listo para inyectarse en el prompt `main` (placeholder
    {shared_info}).

    `mentioned` tiene la forma {categoria: {llave: valor}} (p. ej.
    {"general": {"name": "José González"}}). Se aplana a una lista de
    viñetas "- etiqueta: valor".
    """
    # Etiquetas legibles para las llaves que el paciente puede ir compartiendo
    # (ver el prompt `extract_info`). Definidas dentro de la función porque los
    # plugins se ejecutan con globals restringidos y no ven nombres de módulo.
    labels = {
        "name": "nombre",
        "age": "edad",
        "marital_status": "estado civil",
        "married_years": "años de casado",
        "kids": "hijos/hijas",
        "kids_ages": "edades de los hijos/hijas",
        "wifes_name": "nombre de la esposa",
        "ocupation": "ocupación",
        "household_situation": "situación de vivienda",
    }

    lines = []
    for _category, values in mentioned.items():
        for key, value in values.items():
            label = labels.get(key, key)
            lines.append("- " + str(label) + ": " + str(value))

    if not lines:
        return "Aún no has compartido información con el psicólogo."

    return "\n".join(lines)
