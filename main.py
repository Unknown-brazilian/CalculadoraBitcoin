from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import webbrowser
from backend import calcular


class MainScreen(BoxLayout):
    def calcular_satoshis(self):
        valor_reais = self.ids.valor_reais.text
        desconto = self.ids.desconto.text
        taxa = self.ids.taxa.text

        # Chama o backend para calcular os satoshis
        resultado = calcular(valor_reais, desconto, taxa)
        self.ids.resultado.text = resultado


class CalculadoraBitcoinApp(App):
    def build(self):
        Builder.load_file("main.kv")
        # Carrega o layout a partir do arquivo KV
        return MainScreen()
    def abrir_link(self, url):
        # Abre o link no navegador padrão
        webbrowser.open(url)


if __name__ == "__main__":
    CalculadoraBitcoinApp().run()