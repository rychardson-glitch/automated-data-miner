import csv
import re

def extract_market_data(html_content):
    """
    Extrai nomes de produtos e preços usando expressões regulares.
    Demonstra habilidades de mineração de dados e código profissional para o cliente.
    """
    titles = re.findall(r'class="product-title">(.*?)<', html_content)
    prices = re.findall(r'class="product-price">(.*?)<', html_content)
    
    products = []
    for title, price in zip(titles, prices):
        products.append({
            'Product Name': title.strip(),
            'Price': price.strip()
        })
    return products

def save_to_csv(data, filename="market_data.csv"):
    if not data:
        print("Nenhum dado encontrado para salvar.")
        return
        
    # Garante o funcionamento correto pegando as chaves do primeiro dicionário
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"Dados salvos com sucesso em {filename}")

# Estrutura HTML simulada para demonstrar o funcionamento do script
mock_html = """
<div class="product">
    <h2 class="product-title">Premium Wireless Headphones</h2>
    <span class="product-price">$129.99</span>
</div>
<div class="product">
    <h2 class="product-title">Mechanical Gaming Keyboard</h2>
    <span class="product-price">$89.50</span>
</div>
"""

if __name__ == "__main__":
    print("Iniciando o Minerador de Dados Automatizado...")
    extracted_data = extract_market_data(mock_html)
    save_to_csv(extracted_data)
