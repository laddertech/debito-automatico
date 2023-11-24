# -*- coding: utf-8 -*-

class DebitoAutomaticoError(Exception):
    """Excessao base para o Débito Automático"""


class AtribuicaoCampoError(DebitoAutomaticoError):
    """Tentativa de atribuicao de valor indevido ao campo"""

    def __init__(self, campo, valor):
        self.campo = campo
        self.valor = valor
        super(AtribuicaoCampoError, self).__init__(self)

    def __unicode__(self):
        return 'campo:{0} formato:{1} decimais:{2} digitos:{3} - valor:{4}'. \
            format(
            self.campo.nome,
            self.campo.formato,
            self.campo.decimais,
            self.campo.digitos,
            repr(self.valor),
        )


class NumDigitosExcedidoError(AtribuicaoCampoError):
    """Tentativa de atribuicao de valor mais longo que o campo suportaia"""


class TipoError(AtribuicaoCampoError):
    """Tentativa de atribuicao de tipo nao suportado pelo campo"""


class NumDecimaisError(AtribuicaoCampoError):
    """Numero de casasa decimais em desacordo com especificacao"""


class FaltandoArgsError(DebitoAutomaticoError):
    """Faltando argumentos na chamada do metodo"""

    def __init__(self, args_faltantes):
        self.args_faltantes = args_faltantes
        super(FaltandoArgsError, self).__init__(self)

    def __unicode__(self):
        return ('Os seguintes kwargs sao obrigatorios e nao foram '
                'encontrados: {0}').format(', '.join(self.args_faltantes))


class ArquivoVazioError(DebitoAutomaticoError):
    """Tentativa de escrita de arquivo vazio."""


class CampoObrigatorioError(DebitoAutomaticoError):
    """Campo obrigatorio nao preenchido."""
