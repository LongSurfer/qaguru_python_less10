# относительный путь к файлу
def resource(path):
    import demoqa_tests
    from pathlib import Path
    return str(
        Path(demoqa_tests.__file__)
        .parent
        .parent
        .joinpath(f'resources\{path}')
    )