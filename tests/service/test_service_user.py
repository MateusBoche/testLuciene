from src.service.service_user import ServiceUser

class TestServiceUser:

    def test_add_user_success(self):
        name_add = 'Leonardo'
        job_add = 'TechLead'
        result_expect = 'Usuario adicionado com sucesso'
        service = ServiceUser()

        result = service.add_user(name=name_add, job=job_add)

        assert result_expect == result

    def test_validate_null_job(self):
        name_null = 'Matheus'
        job_null = None
        result_expect = 'Usuario nao adicionado'
        service = ServiceUser()

        result = service.add_user(name=name_null, job=job_null)

        assert result_expect == result

    def test_del_user_success(self):
        service = ServiceUser()
        service.add_user(name="Leonardo", job="TechLead")
        result = service.del_user(name="Leonardo")
        result_expect = "Usuario removido"

        assert result_expect == result


    def test_del_user_nonexistent(self):
        service = ServiceUser()
        result = service.del_user(name="Nonexistent")
        result_expect = "Usuario não encontrado"

        assert result_expect == result

    def test_select_user_success(self):
        service = ServiceUser()
        service.add_user(name="Leonardo", job="TechLead")
        result = service.select_user(name="Leonardo")
        result_expect = "Profissão: TechLead"

        assert result_expect == result

    def test_select_user_nonexistent(self):
        service = ServiceUser()
        result = service.select_user(name="Nonexistent")
        result_expect = "Usuario não encontrado"

        assert result_expect == result


