import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import unicodedata
import re


file_path = "pruebas2.xlsx"
df = pd.read_excel(file_path)


df.columns = df.columns.str.strip()


df.rename(columns={
    '¿Cuál es el rol que desempeña actualmente para la compañía que trabaja?': 'Rol actual',
    '¿Cuántos años de experiencia tiene involucrado en el desarrollo de software?': 'Años de experiencia',
    '¿En qué país se originó la organización para la que trabaja?': 'País origen',
    'La imagen compara dos enfoques de pruebas en software.\n\nLa\xa0pirámide de pruebas\xa0(arriba) representa una estrategia eficiente, con una base sólida de\xa0pruebas unitarias automatizadas, seguidas de\xa0pru...': 'Estrategia preferida'
}, inplace=True)


def limpiar_texto(texto):
    if isinstance(texto, str):
        texto = texto.strip().lower()
        texto = ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
    return texto


def limpiar_experiencia(valor):
    if pd.isna(valor):
        return None
    if isinstance(valor, (int, float)):
        return float(valor)
    match = re.search(r'\d+(\.\d+)?', str(valor))
    return float(match.group()) if match else None


df['País origen'] = df['País origen'].apply(limpiar_texto)
df['Rol actual'] = df['Rol actual'].apply(limpiar_texto)
df['Años de experiencia'] = df['Años de experiencia'].apply(limpiar_experiencia)


plt.figure(figsize=(8, 4))
sns.histplot(df['Años de experiencia'].dropna(), bins=10, kde=True, color='skyblue')
plt.title('Distribución de años de experiencia en desarrollo de software')
plt.xlabel('Años de experiencia')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
sns.boxplot(x='Estrategia preferida', y='Años de experiencia', data=df, palette='Set2')
plt.title('Preferencia de estrategia vs Años de experiencia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
df['País origen'].value_counts().plot(kind='bar', color='salmon')
plt.title('País de origen de la organización')
plt.ylabel('Número de respuestas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.countplot(y='Rol actual', hue='Estrategia preferida', data=df, palette='pastel')
plt.title('Preferencia de estrategia según el rol actual')
plt.xlabel('Cantidad de respuestas')
plt.ylabel('Rol')
plt.legend(title='Estrategia preferida')
plt.tight_layout()
plt.show()
