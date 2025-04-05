import pandas as pd


df = pd.read_excel('pruebas2.xlsx')


df.columns = df.columns.str.strip()


total_respuestas = len(df)


def mostrar_distribucion(serie, titulo):
    conteo = serie.value_counts()
    porcentaje = (conteo / total_respuestas * 100).round(2)
    distribucion = pd.DataFrame({'Cantidad': conteo, 'Porcentaje (%)': porcentaje})
    
    moda = serie.mode().iloc[0] if not serie.mode().empty else None
    nulos = serie.isna().sum()
    categorias_unicas = serie.nunique()
    
    print(f"{titulo}:\n{distribucion}\n")
    print(f"  Moda: {moda}")
    print(f"  Categorías únicas: {categorias_unicas}")
    print(f"  Valores nulos: {nulos}\n")


mostrar_distribucion(df["Por favor seleccione su genero"], "Distribución por género")


mostrar_distribucion(df["Por favor seleccione el rango de edad en el cual se encuentra actualmente:"], "Distribución por rango de edad")


mostrar_distribucion(df["Por favor seleccione su nivel de escolaridad:"], "Nivel de escolaridad")


mostrar_distribucion(df["¿En qué sector (Tecnología, Salud, Finanzas, etc) se ubica la compañia para la que actualmente trabaja?"], "Sector de la compañía")


mostrar_distribucion(df["¿Cuál es el rol que desempeña actualmente para la compañía que trabaja?"], "Rol actual")


experiencia = pd.to_numeric(df["¿Cuántos años de experiencia tiene involucrado en el desarrollo de software?"], errors='coerce')

experiencia_total = experiencia.sum()
experiencia_promedio = experiencia.mean()
experiencia_min = experiencia.min()
experiencia_max = experiencia.max()
experiencia_mediana = experiencia.median()
experiencia_moda = experiencia.mode().iloc[0] if not experiencia.mode().empty else None
experiencia_std = experiencia.std()
experiencia_iqr = experiencia.quantile(0.75) - experiencia.quantile(0.25)
experiencia_nulos = experiencia.isna().sum()

print("Estadísticas de años de experiencia:")
print(f"  Total: {experiencia_total}")
print(f"  Promedio: {experiencia_promedio:.2f}")
print(f"  Mediana: {experiencia_mediana}")
print(f"  Moda: {experiencia_moda}")
print(f"  Mínimo: {experiencia_min}")
print(f"  Máximo: {experiencia_max}")
print(f"  Desviación estándar: {experiencia_std:.2f}")
print(f"  Rango intercuartílico (IQR): {experiencia_iqr}")
print(f"  Valores nulos: {experiencia_nulos}\n")


mostrar_distribucion(df["¿En qué país se originó la organización para la que trabaja?"], "País de origen de la organización")


mostrar_distribucion(
    df["La imagen compara dos enfoques de pruebas en software.\n\nLa pirámide de pruebas (arriba) representa una estrategia eficiente, con una base sólida de pruebas unitarias automatizadas, seguidas de pru..."],
    "Preferencia visual entre pirámide de pruebas y cono"
)


print(f"Total de respuestas analizadas: {total_respuestas}")
