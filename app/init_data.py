
def create_capability(system, capability_data, domain_id, role_id, policy_bypass):
    capability = system.subsystems['capability'].manager.create(**capability_data)
    policy_data = {'domain_id': domain_id, 'capability_id': capability.id, 'role_id': role_id, 'bypass': policy_bypass}
    policy = system.subsystems['policy'].manager.create(**policy_data)


def do(system):
    domain = system.subsystems['domain'].manager.create(name='default')
    user_data = {'name': 'admin', 'email':'admin@example.com', 'password':'123456', 'domain_id': domain.id}
    user = system.subsystems['user'].manager.create(**user_data)
    role = system.subsystems['role'].manager.create(domain_id=domain.id, name='admin')
    system.subsystems['grant'].manager.create(user_id=user.id, role_id=role.id)

    domain = system.subsystems['domain'].manager.create(name='objetorelacional.com.br')
    user_data = {'name': 'admin', 'email':'admin@example.com', 'password':'123456', 'domain_id': domain.id}
    user = system.subsystems['user'].manager.create(**user_data)
    role = system.subsystems['role'].manager.create(domain_id=domain.id, name='admin')
    system.subsystems['grant'].manager.create(user_id=user.id, role_id=role.id)

    # TOKEN
    capability_data = {'name': 'Criar Token', 'url': '/tokens', 'method': 'POST'}
    create_capability(system, capability_data, domain.id, role.id, True)
    capability_data = {'name': 'Remover Token', 'url': '/tokens/<id>', 'method': 'DELETE'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Token', 'url': '/tokens/<id>', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'OPT Token', 'url': '/tokens', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)

    # DOMAIN
    capability_data = {'name': 'Criar Domain', 'url': '/domains', 'method': 'POST'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Atualizar Domain', 'url': '/domains/<id>', 'method': 'PUT'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Remover Domain', 'url': '/domains/<id>', 'method': 'DELETE'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Domain', 'url': '/domains', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Domain', 'url': '/domains/<id>', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'OPT Domain', 'url': '/domains', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)
    capability_data = {'name': 'OPT Domain/<id>', 'url': '/domains/<id>', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)

    # ROLE
    capability_data = {'name': 'Criar Role', 'url': '/roles', 'method': 'POST'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Atualizar Role', 'url': '/roles/<id>', 'method': 'PUT'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Remover Role', 'url': '/roles/<id>', 'method': 'DELETE'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Role', 'url': '/roles', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Role', 'url': '/roles/<id>', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'OPT Role', 'url': '/roles', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)
    capability_data = {'name': 'OPT Role/<id>', 'url': '/roles/<id>', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)

    # USER
    capability_data = {'name': 'Criar User', 'url': '/users', 'method': 'POST'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Atualizar User', 'url': '/users/<id>', 'method': 'PUT'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Remover User', 'url': '/users/<id>', 'method': 'DELETE'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Listar Users', 'url': '/users', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter User', 'url': '/users/<id>', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Restaurar User', 'url': '/users/restore', 'method': 'POST'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Resetar User', 'url': '/users/reset', 'method': 'POST'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Capacidades User', 'url': '/users/capabilitys', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'OPT User', 'url': '/users', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)
    capability_data = {'name': 'OPT User/<id>', 'url': '/users/<id>', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)
    capability_data = {'name': 'OPT Restaurar User', 'url': '/users/restore', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)
    capability_data = {'name': 'OPT Resetar User', 'url': '/users/reset', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)
    capability_data = {'name': 'OPT Obter Capacidades User', 'url': '/users/capabilitys', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)

    # GRANT
    capability_data = {'name': 'Criar Grant', 'url': '/grants', 'method': 'POST'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Atualizar Grant', 'url': '/grants/<id>', 'method': 'PUT'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Remover Grant', 'url': '/grants/<id>', 'method': 'DELETE'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Grant', 'url': '/grants', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Grant', 'url': '/grants/<id>', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'OPT Grant', 'url': '/grants', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)
    capability_data = {'name': 'OPT Grant/<id>', 'url': '/grants/<id>', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)

    # CAPABILITY
    capability_data = {'name': 'Criar Capability', 'url': '/capabilitys', 'method': 'POST'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Atualizar Capability', 'url': '/capabilitys/<id>', 'method': 'PUT'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Remover Capability', 'url': '/capabilitys/<id>', 'method': 'DELETE'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Capability', 'url': '/capabilitys', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Capability', 'url': '/capabilitys/<id>', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'OPT Capability', 'url': '/capabilitys', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)
    capability_data = {'name': 'OPT Capability/<id>', 'url': '/capabilitys/<id>', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)

    # POLICY
    capability_data = {'name': 'Criar Policy', 'url': '/policys', 'method': 'POST'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Atualizar Policy', 'url': '/policys/<id>', 'method': 'PUT'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Remover Policy', 'url': '/policys/<id>', 'method': 'DELETE'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Policy', 'url': '/policys', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Policy', 'url': '/policys/<id>', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'OPT Policy', 'url': '/policys', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)
    capability_data = {'name': 'OPT Policy/<id>', 'url': '/policys/<id>', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)

    # ESTADO
    capability_data = {'name': 'Criar Estado', 'url': '/estados', 'method': 'POST'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Atualizar Estado', 'url': '/estados/<id>', 'method': 'PUT'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Remover Estado', 'url': '/estados/<id>', 'method': 'DELETE'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Estado', 'url': '/estados', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'Obter Estado', 'url': '/estados/<id>', 'method': 'GET'}
    create_capability(system, capability_data, domain.id, role.id, False)
    capability_data = {'name': 'OPT Estado', 'url': '/estados', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)
    capability_data = {'name': 'OPT Estado/<id>', 'url': '/estados/<id>', 'method': 'OPTIONS'}
    create_capability(system, capability_data, domain.id, role.id, True)