<img src="https://github.com/ShiroBrowser/ShiroAssets/blob/main/browser.png">

# 🛡️ Shiro Browser

O **Shiro Browser** é um navegador moderno, focado em privacidade e alta performance, construído com **Python** e o motor **Chromium**. O seu nome (*Shiro* - Branco/Puro em japonês) reflete a nossa filosofia: uma experiência de navegação limpa, sem anúncios intrusivos e extremamente rápida.

Utilizamos o poder da resolução de DNS assíncrona com `aiodns` para garantir que o tempo de carregamento das páginas seja o menor possível.

## 🚀 Funcionalidades Principal

- **Shiro Shield (AdBlock):** Bloqueio nativo de anúncios e rastreadores para uma web mais limpa e segura.
- **DNS Assíncrono:** Integração com `aiodns` para resolução de domínios ultra-rápida.
- **Motor Chromium:** Compatibilidade total com os padrões web modernos (HTML5, CSS3, JS).
- **Interface Minimalista:** Design focado no que importa: o conteúdo.
- **Open Source:** Transparência total sobre como os teus dados são (ou melhor, não são) tratados.

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/) - Linguagem base.
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) - Interface gráfica.
- [QtWebEngine](https://doc.qt.io/qt-6/qtwebengine-index.html) - Motor Chromium.
- [aiodns](https://github.com/saghul/aiodns) - Resolução de DNS assíncrona.

## 📦 Como Instalar e Rodar

### Pré-requisitos
Certifica-te de que tens o Python instalado. Recomenda-se o uso de um ambiente virtual.

### Passo a passo
1. Clone o repositório:
   ```bash
   git clone [https://github.com/ShiroBrowser/shiro-browser.git](https://github.com/ShiroBrowser/shiro-browser.git)
   cd shiro-browser

```

2. Instale as dependências:
```bash
pip install -r requirements.txt

```


3. Execute o navegador:
```bash
python src/main.py

```



## 🌐 Site Oficial

Visite-nos em: [shirobrowser.sh](https://shirobrowser.sh)

## 📄 Licença

Este projeto está licenciado sob a licença MPL 3.0 - consulte o ficheiro [LICENSE](https://github.com/ShiroBrowser/Shiro/blob/LICENSE) para mais detalhes.

---

Inspirado pelo [Brave](https://github.com/Brave) e feito com ❤️ por Astro
