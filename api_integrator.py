import json
import urllib.request

def validate_leads_pipeline(email_list):
    """
    Consome uma API de validação simulada para verificar a autenticidade de e-mails.
    Demonstra arquitetura de integração, tratamento de JSON e filtragem de dados.
    """
    validated_leads = {"valid": [], "invalid": []}
    
    # URL de teste/simulação usando um endpoint público que retorna dados em JSON
    api_url = "https://typicode.com"
    
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            # Transforma a resposta da API em um dicionário Python
            api_data = json.loads(response.read().decode('utf-8'))
            
            # Simulando validação real cruzando os domínios aceitos
            valid_domains = [user['email'].split('@')[-1] for user in api_data]
            
            for email in email_list:
                domain = email.split('@')[-1] if '@' in email else ""
                if domain in valid_domains or ".com" in domain:
                    validated_leads["valid"].append(email)
                else:
                    validated_leads["invalid"].append(email)
                    
        return validated_leads
    except Exception as e:
        print(f"Erro crítico na integração com a API: {e}")
        return None

if __name__ == "__main__":
    print("Iniciando Pipeline de Validação de Leads via API...")
    
    lista_teste = [
        "john.doe@biz.com", 
        "invalid_email_test", 
        "contact@domain.xyz", 
        "support@workspace.org"
    ]
    
    resultado = validate_leads_pipeline(lista_teste)
    if resultado:
        print("\n=== RELATÓRIO DE PROCESSAMENTO ===")
        print(f"Leads Válidos Aprovados: {resultado['valid']}")
        print(f"Leads Inválidos Descartados: {resultado['invalid']}")
