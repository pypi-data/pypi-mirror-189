from src.pg_stage.obfuscator import Obfuscator


def test_parse_copy_values_with_delete_table(obfuscator_object: Obfuscator):
    """
    Arrange: Дамп таблиц, данные которых необходимо удалить
    Act: Вызов функции `_parse_line` класса Obfuscator
    Assert: В stdout нет данных из таблицы
    """
    with open('pg_stage/tests/sql/test_parse_copy_values_with_delete_tables.sql') as file:
        dump_sql = file.read()

    result = []
    for line in dump_sql.splitlines():
        new_line = obfuscator_object._parse_line(line=line)
        if new_line is not None:
            result.append(new_line)

    assert_result = [
        'COMMENT ON TABLE table_1 IS \'anon: {"mutation_name": "delete"}\';',
        'COPY table_1 (id, message, recipient, notes) FROM stdin;',
        '\\.',
        '',
        'COMMENT ON TABLE schema.table_2 IS \'anon: {"mutation_name": "delete"}\';',
        'COPY schema.table_2 (id, message, recipient, notes) FROM stdin;',
        '\\.',
    ]
    assert assert_result == result  # nosec


def test_parse_copy_values_with_mutation(obfuscator_object: Obfuscator):
    """
    Arrange: Дамп таблиц, в которых необходимо мутировать одно или несколько полей
    Act: Вызов функции `_parse_line` класса Obfuscator
    Assert: В stdout данные полей мутированы
    """
    with open('pg_stage/tests/sql/test_parse_copy_values_with_mutation.sql') as file:
        dump_sql = file.read()

    result = set()
    for line in dump_sql.splitlines():
        new_line = obfuscator_object._parse_line(line=line)
        if new_line is not None:
            result.add(new_line)

    assert not (  # nosec
        {'cj@example.com', 'leo@example.com', 'donna@example.com', 'charlie@example.com', 'fun@example.com'} & result
    )
    assert not (  # nosec
        {
            '86a97ff982e87ed5af7d90ab2ce31d4e89a3af3e6a0490b067bb8213aea7a4ee0eeafae1d8fe3c6f990aead095092fcf852004b18'
            'e484ef22569aebf64c3747f',
            '630aaf10f3edcb396181535476bccfd369e1ee9281cbc218d0861e6117b9839219cb403abed3b59468b2564c229d78b0cb610d0e1'
            '6fa4a03dc4d93ed3d55deb3',
            '06fa5d0f3a4d62ff60717ff3315301129a5bcd152f63f073b67d2e6a835b098524b1d097367283c97ca75db9154cf61d6a918248e'
            'b68eaf8cd83d1a87cdd92dc',
            '02cbd8d1e9690c7786375f9f6ec4da6fa3c2ead70d41a7aa1d7fe631477b42635210f0e8fa7579f6f4b5afdb364d9465623a2861e'
            'cff75fa3a052c9b2a9fc2dd',
            'b09909b6e83938dd41ffb5e931eeb3d646b1856dfb74a81acb1697b6d8466468047fe92286e011a4634c71b8d8775c7d5a31e19ce'
            '111bd31d0a61a4faf93d6af',
        }
        & result
    )
    assert not (  # nosec
        {
            'v8BMktHnOeokEBTy6As',
            'c5d6v3NS97D3wYkUltFQ',
            '2IcBeSh6IVVCJyZpqBt',
            'QOqWQ24CMiRNuPUz8f5',
            'uMYA6c3A7uGoI0aEbJ8R',
        }
        & result
    )


def test_parse_copy_values_with_relations(obfuscator_object: Obfuscator):
    """
    Arrange: Дамп таблиц, в которых необходимо мутировать одно связанное поле
    Act: Вызов функции `_parse_line` класса Obfuscator
    Assert: В stdout данные поле мутировано во всех таблицах одинаково и не задета таблица с похожими данными
    """
    with open('pg_stage/tests/sql/test_parse_copy_values_with_relations.sql') as file:
        dump_sql = file.read()

    result = []
    for line in dump_sql.splitlines():
        new_line = obfuscator_object._parse_line(line=line)
        if new_line is not None:
            result.append(new_line)

    index_copy_table4 = result.index('20f654fe-b27d-4051-9fd4-000000000001\t111n\tLourense') - 1
    assert 'table_4' in result[index_copy_table4]  # nosec
    assert (  # nosec
        len([line for line in result if line == '20f654fe-b27d-4051-9fd4-000000000001\t111n\tLourense']) == 1
    )
    assert len([line for line in result if line == '20f654fe-b27d-4051-9fd4-000000000002\t222n\tKent']) == 1  # nosec
    assert (  # nosec
        len({line for line in result if '20f654fe-b27d-4051-9fd4-000000000001' in line and '111n' not in line}) == 1
    )
    assert (  # nosec
        len({line for line in result if '20f654fe-b27d-4051-9fd4-000000000002' in line and '222n' not in line}) == 1
    )
