# Manhattan-Distance-Kata-TDD

Repositorio de práctica de **Test-Driven Development (TDD)**.

## Requisitos

Este repositorio está implementado en Python, usando la herramienta de Testing Pytest:

- [Python](https://www.python.org/downloads/)
- [Pytest](https://docs.pytest.org/en/stable/getting-started.html)

## Instrucciones de Uso

Siga estos pasos:

1. Clonar el repositorio en su máquina local:
    ```bash
    git clone https://github.com/SamEsteb/Manhattan-Distance-Kata-TDD/
    cd Manhattan-Distance-Kata-TDD
    ```

2. Instale la dependencia de pytest utilizando el archivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ``` 

3. Ejecute las pruebas con `pytest` desde el directorio raíz del proyecto:
    ```bash
    pytest
    ```
    ## Inspección de Tests con Tags

    Para explorar los cambios realizados paso a paso durante el desarrollo, se pueden inspeccionar los commits usando Tags.

    ### Lista de Tags Disponibles

    Para listar los tags disponibles, se debe utilizar el siguiente comando:

    ```bash
    git tag
    ```

    Esto mostrará una lista como la siguiente:

    ```
    Test1
    Test2_fail
    Test2_success
    Test3_fail
    Test3_refactorizacion
    Test3_success
    Test4_fail
    Test4_success
    Test5_fail
    Test5_refactorizacion
    Test5_success
    Test6_refactorizacion
    Test6_success
    Test7_refactorizacion
    Test7_success
    ```

    ### Cómo Usar los Tags

    Se puede mover a un punto específico del proceso utilizando el comando `git checkout` seguido del nombre del tag deseado. Por ejemplo:

    ```bash
    git checkout Test1
    ```

    > **Nota:** Reemplazar `Test1` con el nombre del tag al que se quiera dirigir.

    Luego, para volver al estado actual del proyecto, se debe ejecutar:

    ```bash
    git checkout Main
    ```



