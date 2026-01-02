#!/usr/bin/env python3
"""
██████╗ ██╗ ██████╗  ██████╗███████╗██╗     
██╔══██╗██║██╔═══██╗██╔════╝██╔════╝██║     
██████╔╝██║██║   ██║██║     █████╗  ██║     
██╔══██╗██║██║   ██║██║     ██╔══╝  ██║     
██████╔╝██║╚██████╔╝╚██████╗███████╗███████╗
╚═════╝ ╚═╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝
BIO-CEL INTERACTIVE: TERMINAL DEL CONOCIMIENTO CELULAR (Básica)
             -Miguel Martín Gil-
"""

import sys
import os
import json
import random
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum
import pickle

# ===========================================================================
# ESTRUCTURAS DE DATOS BASADAS EN EL PDF
# ===========================================================================

@dataclass
class Tema:
    """Representa un tema del temario"""
    numero: int
    titulo: str
    contenido: List[str] = field(default_factory=list)
    conceptos_clave: List[str] = field(default_factory=list)
    preguntas: List[Dict] = field(default_factory=list)

@dataclass
class PreguntaTest:
    """Pregunta para el sistema de evaluación"""
    tema: int
    enunciado: str
    opciones: List[str]
    respuesta_correcta: int  # índice 0-based
    explicacion: str
    nivel_dificultad: str = "medio"  # facil, medio, dificil

class SistemaEstudio:
    """Sistema principal de estudio organizado por temas"""
    
    def __init__(self):
        self.temas = {}
        self.progreso = {}
        self.historial_tests = []
        self.notas = {}
        self.cargar_temario()
        self.cargar_progreso()
    
    def cargar_temario(self):
        """Carga el temario completo basado en el PDF"""
        
        # TEMA 1: Eucariotas y Procariotas
        tema1 = Tema(
            numero=1,
            titulo="Eucariotas y Procariotas",
            conceptos_clave=[
                "Procariotas: sin núcleo, estructura sencilla",
                "Eubacterias: pared de mureína, hábitats normales",
                "Arqueobacterias: hábitats extremos",
                "Estructuras bacterianas: pared, cápsula, flagelos, plásmidos",
                "Eucariotas: núcleo, orgánulos membranosos, citoesqueleto",
                "Diferencias animal/vegetal"
            ]
        )
        
        # TEMA 2: Membrana Plasmática
        tema2 = Tema(
            numero=2,
            titulo="Membrana Plasmática",
            conceptos_clave=[
                "Bicapa lipídica: fosfolípidos, colesterol, esfingolípidos",
                "Proteínas de membrana: integrales, periféricas, ancladas",
                "Glucocálix: glucoproteínas y glucolípidos",
                "Fluidez y asimetría de membrana",
                "Microdominios lipídicos (lipid rafts)",
                "Grupos sanguíneos: antígenos A, B, H"
            ]
        )
        
        # TEMA 3: Transporte a través de Membrana
        tema3 = Tema(
            numero=3,
            titulo="Transporte de Moléculas a través de la Membrana",
            conceptos_clave=[
                "Difusión simple y ósmosis",
                "Transporte pasivo: permeasas, canales",
                "Transporte activo: bombas ATPasas",
                "Bomba Na+/K+ ATPasa",
                "Potencial de membrana y potencial de acción",
                "Transporte secundario: simport, antiport"
            ]
        )
        
        # TEMA 4: Matriz Extracelular y Pared Celular
        tema4 = Tema(
            numero=4,
            titulo="Matriz Extracelular y Pared Celular",
            conceptos_clave=[
                "GAGs: ácido hialurónico, condroitín sulfato",
                "Proteoglicanos y glicoproteínas",
                "Colágeno: tipos, estructura, síntesis",
                "Elastina y fibronectina",
                "Enfermedades: osteogénesis imperfecta, síndrome de Marfan",
                "Pared vegetal: celulosa, hemicelulosa, pectina"
            ]
        )
        
        # TEMA 5: Uniones y Adhesión Celular
        tema5 = Tema(
            numero=5,
            titulo="Uniones y Adhesión Celular",
            conceptos_clave=[
                "Uniones herméticas (oclusivas)",
                "Uniones adherentes (ancorantes)",
                "Desmosomas y hemidesmosomas",
                "Uniones comunicantes (GAP)",
                "Plasmodesmas (vegetales)",
                "CAMs: cadherinas, integrinas, selectinas"
            ]
        )
        
        # TEMA 6: Microfilamentos
        tema6 = Tema(
            numero=6,
            titulo="Microfilamentos",
            conceptos_clave=[
                "Actina G y Actina F",
                "Polimerización de actina",
                "Proteínas reguladoras: ARP, formina, cofilina",
                "Miosinas: tipos I y II",
                "Contracción muscular",
                "Toxinas: citocalasina, latrunculina"
            ]
        )
        
        # TEMA 7: Microtúbulos
        tema7 = Tema(
            numero=7,
            titulo="Microtúbulos",
            conceptos_clave=[
                "Tubulinas α y β",
                "Centrosoma y centriolos",
                "Polimerización e inestabilidad dinámica",
                "Proteínas asociadas: MAPs, tau",
                "Proteínas motoras: quinesinas, dineinas",
                "Cilios y flagelos: axonema, corpúsculo basal"
            ]
        )
        
        # TEMA 8: Filamentos Intermedios
        tema8 = Tema(
            numero=8,
            titulo="Filamentos Intermedios",
            conceptos_clave=[
                "Tipos: queratina, desmina, vimentina, neurofilamentos, láminas",
                "Estructura fibrosa (no globular)",
                "Sin polaridad ni proteínas motoras",
                "Polimerización y despolimerización",
                "Enfermedades: epidermólisis bullosa, ELA"
            ]
        )
        
        # TEMA 9: Compartimentos Intracelulares
        tema9 = Tema(
            numero=9,
            titulo="Compartimentos Intracelulares y Transporte de Proteínas",
            conceptos_clave=[
                "Origen de orgánulos membranosos",
                "Teoría endosimbiótica",
                "Importación cotraduccional y postraduccional",
                "Señales de direccionamiento",
                "Transporte vesicular"
            ]
        )
        
        # TEMA 10: Núcleo
        tema10 = Tema(
            numero=10,
            titulo="Núcleo",
            conceptos_clave=[
                "Envoltura nuclear: membranas interna y externa",
                "Poros nucleares y transporte activo",
                "NLS (Nuclear Localization Signal)",
                "Importinas y exportinas",
                "Nucleolo: síntesis de rRNA",
                "Cromatina: eucromatina y heterocromatina"
            ]
        )
        
        # TEMA 11: Citosol
        tema11 = Tema(
            numero=11,
            titulo="Citosol",
            conceptos_clave=[
                "Plegamiento de proteínas",
                "Chaperonas: hsp70 y hsp60",
                "Degradación por ubiquitina-proteosoma",
                "Modificaciones postraduccionales",
                "Enfermedades por mal plegamiento"
            ]
        )
        
        # TEMA 12: Retículo Endoplasmático
        tema12 = Tema(
            numero=12,
            titulo="Retículo Endoplasmático",
            conceptos_clave=[
                "RER y REL: diferencias funcionales",
                "Síntesis de lípidos en REL",
                "Síntesis de proteínas en RER",
                "Glicosilación N-unida",
                "Control de calidad de proteínas",
                "Enfermedades: fibrosis quística, enfisema"
            ]
        )
        
        # TEMA 13: Aparato de Golgi
        tema13 = Tema(
            numero=13,
            titulo="Aparato de Golgi",
            conceptos_clave=[
                "Estructura: cis, medial, trans",
                "Modificaciones de oligosacáridos",
                "Señal M6P para hidrolasas lisosomales",
                "Secreción constitutiva y regulada",
                "Transporte vesicular: COP I, COP II, clatrina"
            ]
        )
        
        # TEMA 14: Endosomas, Lisosomas, Vacuolas
        tema14 = Tema(
            numero=14,
            titulo="Endosomas, Lisosomas, Vacuolas",
            conceptos_clave=[
                "Endocitosis: fagocitosis y pinocitosis",
                "Endosomas tempranos y tardíos",
                "Autofagia: selectiva y no selectiva",
                "Enfermedades de acumulación lisosomal",
                "Vacuola vegetal: presión de turgencia"
            ]
        )
        
        # TEMA 15: Mitocondrias
        tema15 = Tema(
            numero=15,
            titulo="Mitocondrias",
            conceptos_clave=[
                "Estructura: membrana externa, interna, matriz",
                "Teoría endosimbiótica",
                "Cadena transportadora de electrones",
                "Fosforilación oxidativa",
                "ATP sintasa",
                "Enfermedades mitocondriales: MERRF, MELAS"
            ]
        )
        
        # TEMA 16: Peroxisomas
        tema16 = Tema(
            numero=16,
            titulo="Peroxisomas",
            conceptos_clave=[
                "Beta-oxidación de ácidos grasos",
                "Catalasa y detoxificación",
                "Fotorrespiración en plantas",
                "Ciclo del glioxilato",
                "Enfermedades: síndrome de Zellweger"
            ]
        )
        
        # TEMA 17: Señalización Celular
        tema17 = Tema(
            numero=17,
            titulo="Señalización Celular",
            conceptos_clave=[
                "Receptores de superficie e intracelulares",
                "Proteínas G y segundos mensajeros",
                "Receptores tirosina quinasa",
                "Vía Ras/MAPK",
                "Regulación del ciclo celular"
            ]
        )
        
        # TEMA 18: Ciclo Celular
        tema18 = Tema(
            numero=18,
            titulo="Ciclo Celular",
            conceptos_clave=[
                "Fases: G1, S, G2, M",
                "Puntos de control (checkpoints)",
                "Complejos ciclina-Cdk",
                "Proteínas p53 y p21",
                "Retinoblastoma y cáncer"
            ]
        )
        
        # TEMA 19: Mitosis
        tema19 = Tema(
            numero=19,
            titulo="Mitosis",
            conceptos_clave=[
                "Profase: condensación cromosómica",
                "Metafase: placa ecuatorial",
                "Anafase: separación cromátidas",
                "Telofase: reconstrucción nuclear",
                "Citocinesis: anillo contráctil o placa celular"
            ]
        )
        
        # TEMA 20: Meiosis
        tema20 = Tema(
            numero=20,
            titulo="Meiosis",
            conceptos_clave=[
                "Reducción cromosómica: diploide → haploide",
                "Recombinación genética y quiasmas",
                "Gametogénesis: espermatogénesis y ovogénesis",
                "Complejo sinaptonémico",
                "Aneuploidías: síndromes genéticos"
            ]
        )
        
        # Almacenar todos los temas
        self.temas = {
            1: tema1, 2: tema2, 3: tema3, 4: tema4, 5: tema5,
            6: tema6, 7: tema7, 8: tema8, 9: tema9, 10: tema10,
            11: tema11, 12: tema12, 13: tema13, 14: tema14, 15: tema15,
            16: tema16, 17: tema17, 18: tema18, 19: tema19, 20: tema20
        }
        
        # Cargar preguntas para cada tema
        self.cargar_preguntas()
    
    def cargar_preguntas(self):
        """Carga preguntas de test para cada tema"""
        
        # TEMA 1
        self.temas[1].preguntas = [
            {
                "enunciado": "¿Cuál es la principal diferencia estructural entre células eucariotas y procariotas?",
                "opciones": [
                    "Presencia de ribosomas",
                    "Presencia de membrana plasmática",
                    "Presencia de núcleo definido",
                    "Presencia de ADN"
                ],
                "respuesta": 2,
                "explicacion": "Los eucariotas tienen un núcleo verdadero rodeado por membrana nuclear, mientras que los procariotas carecen de núcleo definido."
            },
            {
                "enunciado": "¿Qué componente forma la pared celular de las eubacterias?",
                "opciones": [
                    "Celulosa",
                    "Quitina",
                    "Mureína",
                    "Silicio"
                ],
                "respuesta": 2,
                "explicacion": "Las eubacterias tienen pared celular de mureína (peptidoglicano), que es específica de este grupo."
            },
            {
                "enunciado": "¿Dónde se encuentran típicamente las arqueobacterias?",
                "opciones": [
                    "Ambientes acuáticos normales",
                    "Suelos agrícolas",
                    "Hábitats extremos",
                    "Interior de organismos"
                ],
                "respuesta": 2,
                "explicacion": "Las arqueobacterias son conocidas por habitar ambientes extremos como fuentes termales, ambientes hiperalinos o anaeróbicos."
            }
        ]
        
        # TEMA 2
        self.temas[2].preguntas = [
            {
                "enunciado": "¿Qué molécula modula la fluidez de la membrana en células animales?",
                "opciones": [
                    "Colesterol",
                    "Glucosa",
                    "ADN",
                    "ATP"
                ],
                "respuesta": 0,
                "explicacion": "El colesterol se intercala entre los fosfolípidos, modulando la fluidez de la membrana y evitando que se vuelva demasiado rígida o demasiado fluida."
            },
            {
                "enunciado": "¿Qué técnica permite estudiar la movilidad de moléculas en la membrana?",
                "opciones": [
                    "PCR",
                    "Western blot",
                    "FRAP",
                    "Electroforesis"
                ],
                "respuesta": 2,
                "explicacion": "FRAP (Fluorescence Recovery After Photobleaching) permite medir la difusión lateral de moléculas marcadas con fluorescencia en la membrana plasmática."
            }
        ]
        
        # TEMA 3
        self.temas[3].preguntas = [
            {
                "enunciado": "¿Cuál es la estequiometría de la bomba Na+/K+ ATPasa?",
                "opciones": [
                    "2 Na+ fuera, 3 K+ dentro",
                    "3 Na+ fuera, 2 K+ dentro",
                    "2 Na+ dentro, 3 K+ fuera",
                    "3 Na+ dentro, 2 K+ fuera"
                ],
                "respuesta": 1,
                "explicacion": "La bomba Na+/K+ ATPasa transporta 3 Na+ hacia el exterior y 2 K+ hacia el interior por cada molécula de ATP hidrolizada."
            },
            {
                "enunciado": "¿Qué tipo de transporte utiliza el gradiente de Na+ para mover glucosa?",
                "opciones": [
                    "Difusión simple",
                    "Transporte activo primario",
                    "Transporte activo secundario",
                    "Ósmosis"
                ],
                "respuesta": 2,
                "explicacion": "El cotransporte Na+/glucosa es un transporte activo secundario que utiliza el gradiente de Na+ establecido por la bomba Na+/K+ ATPasa."
            }
        ]
        
        # TEMA 4
        self.temas[4].preguntas = [
            {
                "enunciado": "¿Qué enfermedad está causada por mutaciones en el colágeno tipo I?",
                "opciones": [
                    "Síndrome de Marfan",
                    "Osteogénesis imperfecta",
                    "Escorbuto",
                    "Distrofia muscular"
                ],
                "respuesta": 1,
                "explicacion": "La osteogénesis imperfecta (enfermedad de los huesos de cristal) resulta de mutaciones en los genes que codifican el colágeno tipo I."
            },
            {
                "enunciado": "¿Qué componente principal de la pared vegetal proporciona resistencia a la tracción?",
                "opciones": [
                    "Pectina",
                    "Hemicelulosa",
                    "Celulosa",
                    "Lignina"
                ],
                "respuesta": 2,
                "explicacion": "La celulosa forma microfibrillas que proporcionan resistencia mecánica a la pared celular vegetal."
            }
        ]
        
        # TEMA 15
        self.temas[15].preguntas = [
            {
                "enunciado": "¿En qué compartimento mitocondrial se localiza la cadena respiratoria?",
                "opciones": [
                    "Membrana externa",
                    "Membrana interna",
                    "Matriz",
                    "Espacio intermembrana"
                ],
                "respuesta": 1,
                "explicacion": "Los complejos de la cadena transportadora de electrones están embebidos en la membrana interna mitocondrial."
            },
            {
                "enunciado": "¿Cuál es el producto final de la fosforilación oxidativa?",
                "opciones": [
                    "NADH",
                    "FADH2",
                    "ATP",
                    "CO2"
                ],
                "respuesta": 2,
                "explicacion": "La fosforilación oxidativa utiliza la energía del gradiente de protones para sintetizar ATP a partir de ADP y Pi."
            }
        ]
        
        # TEMA 19
        self.temas[19].preguntas = [
            {
                "enunciado": "¿En qué fase de la mitosis se alinean los cromosomas en la placa ecuatorial?",
                "opciones": [
                    "Profase",
                    "Metafase",
                    "Anafase",
                    "Telofase"
                ],
                "respuesta": 1,
                "explicacion": "En la metafase, todos los cromosomas se alinean en el plano ecuatorial del huso mitótico, formando la placa metafásica."
            },
            {
                "enunciado": "¿Qué proteína mantiene unidas las cromátidas hermanas durante la mitosis?",
                "opciones": [
                    "Condensina",
                    "Cohesina",
                    "Tubulina",
                    "Actina"
                ],
                "respuesta": 1,
                "explicacion": "Las cohesinas mantienen unidas las cromátidas hermanas desde la fase S hasta la anafase, cuando son escindidas por la separasa."
            }
        ]
    
    def cargar_progreso(self):
        """Carga el progreso guardado del estudiante"""
        try:
            with open('progreso_biocel.pkl', 'rb') as f:
                data = pickle.load(f)
                self.progreso = data.get('progreso', {})
                self.historial_tests = data.get('historial', [])
                self.notas = data.get('notas', {})
        except FileNotFoundError:
            # Inicializar progreso si no existe
            for tema_num in self.temas.keys():
                self.progreso[tema_num] = {
                    'estudiado': False,
                    'horas_estudio': 0,
                    'tests_completados': 0,
                    'mejor_nota': 0
                }
    
    def guardar_progreso(self):
        """Guarda el progreso del estudiante"""
        data = {
            'progreso': self.progreso,
            'historial': self.historial_tests,
            'notas': self.notas
        }
        with open('progreso_biocel.pkl', 'wb') as f:
            pickle.dump(data, f)

# ===========================================================================
# INTERFAZ DE CONSOLA LIMPIA Y PROFESIONAL
# ===========================================================================

class InterfazEstudio:
    """Interfaz de línea de comandos para el sistema de estudio"""
    
    def __init__(self):
        self.sistema = SistemaEstudio()
        self.menu_principal()
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de forma multiplataforma"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_encabezado(self, titulo):
        """Muestra un encabezado limpio"""
        self.limpiar_pantalla()
        print("=" * 70)
        print("""
              ██████╗ ██╗ ██████╗  ██████╗███████╗██╗     
              ██╔══██╗██║██╔═══██╗██╔════╝██╔════╝██║     
              ██████╔╝██║██║   ██║██║     █████╗  ██║     
              ██╔══██╗██║██║   ██║██║     ██╔══╝  ██║     
              ██████╔╝██║╚██████╔╝╚██████╗███████╗███████╗
              ╚═════╝ ╚═╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝
""")
        print(f"{'SISTEMA DE ESTUDIO DE BIOLOGÍA CELULAR':^70}")
        print(f"{'Grado en Biología - Curso 2025-2026 - Miguel M.G.':^70}")
        print("=" * 70)
        print(f"\n{titulo}\n")
        print("-" * 70)
    
    def menu_principal(self):
        """Menú principal del sistema"""
        while True:
            self.mostrar_encabezado("MENÚ PRINCIPAL")
            
            print("Opciones disponibles:")
            print("1. Consultar temario completo")
            print("2. Estudiar tema específico")
            print("3. Realizar test por tema")
            print("4. Ver progreso de estudio")
            print("5. Resumen de conceptos clave")
            print("6. Simulación de procesos celulares")
            print("7. Salir del sistema")
            print("-" * 70)
            
            opcion = input("\nSeleccione una opción (1-7): ").strip()
            
            if opcion == "1":
                self.mostrar_temario()
            elif opcion == "2":
                self.estudiar_tema()
            elif opcion == "3":
                self.realizar_test()
            elif opcion == "4":
                self.ver_progreso()
            elif opcion == "5":
                self.resumen_conceptos()
            elif opcion == "6":
                self.simulacion_procesos()
            elif opcion == "7":
                print("\nGuardando progreso...")
                self.sistema.guardar_progreso()
                print("Sistema cerrado correctamente.")
                break
            else:
                input("\nOpción no válida. Presione Enter para continuar...")
    
    def mostrar_temario(self):
        """Muestra el temario completo organizado"""
        self.mostrar_encabezado("TEMARIO COMPLETO")
        
        print("Temas del curso de Biología Celular:")
        print()
        
        for tema_num in sorted(self.sistema.temas.keys()):
            tema = self.sistema.temas[tema_num]
            estudiado = "✓" if self.sistema.progreso.get(tema_num, {}).get('estudiado', False) else " "
            print(f"  [{estudiado}] TEMA {tema_num:2d}: {tema.titulo}")
        
        print("\n" + "-" * 70)
        print("Leyenda: ✓ = Tema estudiado")
        print("-" * 70)
        
        input("\nPresione Enter para volver al menú principal...")
    
    def estudiar_tema(self):
        """Permite estudiar un tema específico"""
        self.mostrar_encabezado("ESTUDIAR TEMA ESPECÍFICO")
        
        print("Seleccione el número del tema que desea estudiar (1-20):")
        print("0. Volver al menú principal")
        print("-" * 70)
        
        try:
            seleccion = int(input("\nTema: "))
            
            if seleccion == 0:
                return
            
            if seleccion not in self.sistema.temas:
                print(f"\nError: El tema {seleccion} no existe.")
                input("Presione Enter para continuar...")
                return
            
            tema = self.sistema.temas[seleccion]
            
            # Registrar inicio de estudio
            if seleccion not in self.sistema.progreso:
                self.sistema.progreso[seleccion] = {
                    'estudiado': False,
                    'horas_estudio': 0,
                    'tests_completados': 0,
                    'mejor_nota': 0
                }
            
            self.mostrar_contenido_tema(tema)
            
        except ValueError:
            print("\nError: Debe ingresar un número válido.")
            input("Presione Enter para continuar...")
    
    def mostrar_contenido_tema(self, tema):
        """Muestra el contenido detallado de un tema"""
        while True:
            self.mostrar_encabezado(f"TEMA {tema.numero}: {tema.titulo}")
            
            print("CONCEPTOS CLAVE:")
            print("-" * 70)
            
            for i, concepto in enumerate(tema.conceptos_clave, 1):
                print(f"{i:2d}. {concepto}")
            
            print("\n" + "=" * 70)
            print("\nOpciones:")
            print("1. Ver preguntas de este tema")
            print("2. Marcar como estudiado")
            print("3. Volver a selección de temas")
            print("-" * 70)
            
            opcion = input("\nSeleccione opción (1-3): ").strip()
            
            if opcion == "1":
                self.mostrar_preguntas_tema(tema)
            elif opcion == "2":
                self.sistema.progreso[tema.numero]['estudiado'] = True
                print(f"\n✓ Tema {tema.numero} marcado como estudiado.")
                input("Presione Enter para continuar...")
            elif opcion == "3":
                break
    
    def mostrar_preguntas_tema(self, tema):
        """Muestra las preguntas disponibles para un tema"""
        if not tema.preguntas:
            print(f"\nNo hay preguntas disponibles para el Tema {tema.numero}.")
            input("Presione Enter para continuar...")
            return
        
        self.mostrar_encabezado(f"PREGUNTAS - TEMA {tema.numero}: {tema.titulo}")
        
        print(f"Total de preguntas disponibles: {len(tema.preguntas)}")
        print("-" * 70)
        
        for i, pregunta in enumerate(tema.preguntas, 1):
            print(f"\nPregunta {i}: {pregunta['enunciado']}")
            print("\nOpciones:")
            for j, opcion in enumerate(pregunta['opciones']):
                print(f"  {chr(65+j)}. {opcion}")
            
            respuesta = input("\n¿Cuál es la respuesta correcta? (A-D): ").strip().upper()
            
            if respuesta in ['A', 'B', 'C', 'D']:
                indice_respuesta = ord(respuesta) - 65
                if indice_respuesta == pregunta['respuesta']:
                    print("\n✓ CORRECTO")
                else:
                    print(f"\n✗ INCORRECTO. La respuesta correcta es: {chr(65 + pregunta['respuesta'])}")
                
                print(f"\nExplicación: {pregunta['explicacion']}")
            else:
                print("\nRespuesta no válida.")
            
            input("\nPresione Enter para continuar...")
            self.limpiar_pantalla()
            self.mostrar_encabezado(f"PREGUNTAS - TEMA {tema.numero}: {tema.titulo}")
    
    def realizar_test(self):
        """Realiza un test sobre un tema específico"""
        self.mostrar_encabezado("TEST DE EVALUACIÓN")
        
        print("Seleccione el tema para el test (1-20):")
        print("0. Volver al menú principal")
        print("-" * 70)
        
        try:
            tema_num = int(input("\nTema: "))
            
            if tema_num == 0:
                return
            
            if tema_num not in self.sistema.temas:
                print(f"\nError: El tema {tema_num} no existe.")
                input("Presione Enter para continuar...")
                return
            
            tema = self.sistema.temas[tema_num]
            
            if not tema.preguntas:
                print(f"\nNo hay preguntas disponibles para el Tema {tema_num}.")
                input("Presione Enter para continuar...")
                return
            
            # Seleccionar preguntas aleatorias
            preguntas_test = random.sample(tema.preguntas, min(5, len(tema.preguntas)))
            
            self.ejecutar_test(tema, preguntas_test)
            
        except ValueError:
            print("\nError: Debe ingresar un número válido.")
            input("Presione Enter para continuar...")
    
    def ejecutar_test(self, tema, preguntas):
        """Ejecuta un test con las preguntas proporcionadas"""
        respuestas_correctas = 0
        respuestas_usuario = []
        
        self.mostrar_encabezado(f"TEST - TEMA {tema.numero}: {tema.titulo}")
        
        print(f"Test de {len(preguntas)} preguntas")
        print("Responda con A, B, C o D")
        print("-" * 70)
        
        for i, pregunta in enumerate(preguntas, 1):
            print(f"\nPregunta {i}/{len(preguntas)}:")
            print(f"{pregunta['enunciado']}")
            print("\nOpciones:")
            
            for j, opcion in enumerate(pregunta['opciones']):
                print(f"  {chr(65+j)}. {opcion}")
            
            while True:
                respuesta = input("\nSu respuesta (A-D): ").strip().upper()
                if respuesta in ['A', 'B', 'C', 'D']:
                    break
                print("Por favor, ingrese A, B, C o D")
            
            indice_respuesta = ord(respuesta) - 65
            respuestas_usuario.append(indice_respuesta)
            
            if indice_respuesta == pregunta['respuesta']:
                respuestas_correctas += 1
        
        # Calcular nota
        nota = (respuestas_correctas / len(preguntas)) * 100
        
        # Mostrar resultados
        self.mostrar_encabezado("RESULTADOS DEL TEST")
        
        print(f"Tema evaluado: TEMA {tema.numero}: {tema.titulo}")
        print(f"Preguntas totales: {len(preguntas)}")
        print(f"Respuestas correctas: {respuestas_correctas}")
        print(f"Nota obtenida: {nota:.1f}/100")
        print("-" * 70)
        
        # Mostrar respuestas incorrectas con explicación
        if respuestas_correctas < len(preguntas):
            print("\nPreguntas con error:")
            for i, (pregunta, respuesta_usuario) in enumerate(zip(preguntas, respuestas_usuario), 1):
                if respuesta_usuario != pregunta['respuesta']:
                    print(f"\nPregunta {i}: {pregunta['enunciado']}")
                    print(f"Su respuesta: {chr(65 + respuesta_usuario)}")
                    print(f"Respuesta correcta: {chr(65 + pregunta['respuesta'])}")
                    print(f"Explicación: {pregunta['explicacion']}")
        
        # Actualizar progreso
        self.sistema.progreso[tema.numero]['tests_completados'] += 1
        if nota > self.sistema.progreso[tema.numero]['mejor_nota']:
            self.sistema.progreso[tema.numero]['mejor_nota'] = nota
        
        # Registrar en historial
        registro = {
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'tema': tema.numero,
            'preguntas_totales': len(preguntas),
            'correctas': respuestas_correctas,
            'nota': nota
        }
        self.sistema.historial_tests.append(registro)
        
        print("\n" + "=" * 70)
        input("\nPresione Enter para volver al menú principal...")
    
    def ver_progreso(self):
        """Muestra el progreso de estudio del usuario"""
        self.mostrar_encabezado("PROGRESO DE ESTUDIO")
        
        print(f"{'TEMA':<6} {'ESTUDIADO':<10} {'TESTS':<6} {'MEJOR NOTA':<12}")
        print("-" * 40)
        
        for tema_num in sorted(self.sistema.temas.keys()):
            progreso = self.sistema.progreso.get(tema_num, {})
            estudiado = "Sí" if progreso.get('estudiado', False) else "No"
            tests = progreso.get('tests_completados', 0)
            mejor_nota = progreso.get('mejor_nota', 0)
            
            print(f"{tema_num:<6} {estudiado:<10} {tests:<6} {mejor_nota:<12.1f}")
        
        print("\n" + "=" * 70)
        
        # Estadísticas generales
        temas_estudiados = sum(1 for p in self.sistema.progreso.values() if p.get('estudiado', False))
        tests_totales = sum(p.get('tests_completados', 0) for p in self.sistema.progreso.values())
        
        print(f"\nRESUMEN:")
        print(f"  Temas estudiados: {temas_estudiados}/20 ({temas_estudiados/20*100:.1f}%)")
        print(f"  Tests completados: {tests_totales}")
        print(f"  Tests en historial: {len(self.sistema.historial_tests)}")
        
        if self.sistema.historial_tests:
            print(f"\nÚLTIMOS TESTS:")
            for test in self.sistema.historial_tests[-3:]:  # Mostrar últimos 3
                print(f"  {test['fecha']} - Tema {test['tema']}: {test['nota']:.1f}/100")
        
        print("\n" + "=" * 70)
        input("\nPresione Enter para volver al menú principal...")
    
    def resumen_conceptos(self):
        """Muestra un resumen de conceptos clave organizado por categorías"""
        self.mostrar_encabezado("RESUMEN DE CONCEPTOS CLAVE")
        
        categorias = {
            "ESTRUCTURA CELULAR": [1, 4, 5],
            "MEMBRANA Y TRANSPORTE": [2, 3],
            "CITOESQUELETO": [6, 7, 8],
            "ORGÁNULOS CELULARES": [9, 10, 11, 12, 13, 14, 15, 16],
            "REGULACIÓN CELULAR": [17, 18, 19, 20]
        }
        
        for categoria, temas_nums in categorias.items():
            print(f"\n{categoria}:")
            print("-" * 70)
            
            for tema_num in temas_nums:
                if tema_num in self.sistema.temas:
                    tema = self.sistema.temas[tema_num]
                    print(f"\nTema {tema_num}: {tema.titulo}")
                    
                    # Mostrar primeros 3 conceptos clave
                    for concepto in tema.conceptos_clave[:3]:
                        print(f"  • {concepto}")
            
            print()
        
        print("=" * 70)
        input("\nPresione Enter para volver al menú principal...")
    
    def simulacion_procesos(self):
        """Simulaciones de procesos celulares básicos"""
        while True:
            self.mostrar_encabezado("SIMULACIÓN DE PROCESOS CELULARES")
            
            print("Seleccione un proceso para simular:")
            print("1. Transporte activo Na+/K+")
            print("2. Cadena respiratoria mitocondrial")
            print("3. Ciclo celular y puntos de control")
            print("4. Regreso al menú principal")
            print("-" * 70)
            
            opcion = input("\nSeleccione opción (1-4): ").strip()
            
            if opcion == "1":
                self.simular_transporte_na_k()
            elif opcion == "2":
                self.simular_cadena_respiratoria()
            elif opcion == "3":
                self.simular_ciclo_celular()
            elif opcion == "4":
                break
    
    def simular_transporte_na_k(self):
        """Simula el funcionamiento de la bomba Na+/K+ ATPasa"""
        self.mostrar_encabezado("SIMULACIÓN: BOMBA Na+/K+ ATPasa")
        
        print("La bomba Na+/K+ ATPasa mantiene los gradientes iónicos:")
        print("  - Expulsa 3 Na+ hacia el exterior")
        print("  - Importa 2 K+ hacia el interior")
        print("  - Consume 1 ATP por ciclo")
        print("-" * 70)
        
        na_int = 10  # mM intracelular
        k_int = 140  # mM intracelular
        na_ext = 145  # mM extracelular
        k_ext = 4    # mM extracelular
        atp = 100    # unidades de ATP
        
        print("\nEstado inicial:")
        print(f"  Na+ intracelular: {na_int} mM")
        print(f"  K+ intracelular: {k_int} mM")
        print(f"  Na+ extracelular: {na_ext} mM")
        print(f"  K+ extracelular: {k_ext} mM")
        print(f"  ATP disponible: {atp} unidades")
        
        print("\nPresione Enter para simular 10 ciclos de la bomba...")
        input()
        
        for ciclo in range(1, 11):
            if atp > 0:
                na_int -= 3
                k_int += 2
                na_ext += 3
                k_ext -= 2
                atp -= 1
                
                # Asegurar valores mínimos
                na_int = max(na_int, 5)
                k_ext = max(k_ext, 2)
                
                print(f"\nCiclo {ciclo}:")
                print(f"  Na+ intracelular: {na_int} mM")
                print(f"  K+ intracelular: {k_int} mM")
                print(f"  ATP restante: {atp} unidades")
        
        print("\n" + "=" * 70)
        print("RESULTADO FINAL:")
        print(f"Gradiente de Na+: {na_ext/na_int:.1f} veces mayor en exterior")
        print(f"Gradiente de K+: {k_int/k_ext:.1f} veces mayor en interior")
        print(f"Potencial de membrana aproximado: -70 mV")
        
        input("\nPresione Enter para continuar...")
    
    def simular_cadena_respiratoria(self):
        """Simula la cadena transportadora de electrones"""
        self.mostrar_encabezado("SIMULACIÓN: CADENA RESPIRATORIA")
        
        print("Complejos de la cadena respiratoria:")
        print("  1. NADH deshidrogenasa (Complejo I)")
        print("  2. Succinato deshidrogenasa (Complejo II)")
        print("  3. Citocromo bc1 (Complejo III)")
        print("  4. Citocromo c oxidasa (Complejo IV)")
        print("-" * 70)
        
        print("\nFlujo de electrones y translocación de protones:")
        print("  NADH → Complejo I → Q → Complejo III → Cit c → Complejo IV → O2")
        print("  FADH2 → Complejo II → Q → Complejo III → Cit c → Complejo IV → O2")
        print("-" * 70)
        
        nadh = 10
        fadh2 = 6
        protones_matriz = 0
        protones_intermembrana = 0
        atp_producido = 0
        
        print("\nEstado inicial:")
        print(f"  NADH disponible: {nadh}")
        print(f"  FADH2 disponible: {fadh2}")
        print(f"  ATP producido: {atp_producido}")
        
        print("\nPresione Enter para comenzar la simulación...")
        input()
        
        # Procesar NADH
        for i in range(min(5, nadh)):
            protones_intermembrana += 10  # 4(I) + 4(III) + 2(IV)
            atp_producido += 2.5  # 10 protones / 4 por ATP
            print(f"\nNADH {i+1}: +10 H+ al espacio intermembrana, ATP total: {atp_producido:.1f}")
        
        # Procesar FADH2
        for i in range(min(3, fadh2)):
            protones_intermembrana += 6  # 0(II) + 4(III) + 2(IV)
            atp_producido += 1.5  # 6 protones / 4 por ATP
            print(f"\nFADH2 {i+1}: +6 H+ al espacio intermembrana, ATP total: {atp_producido:.1f}")
        
        print("\n" + "=" * 70)
        print("RESULTADO FINAL:")
        print(f"  Protones translocados: {protones_intermembrana}")
        print(f"  ATP total producido: {atp_producido:.1f}")
        print(f"  Eficiencia: {(atp_producido/(nadh*2.5 + fadh2*1.5))*100:.1f}%")
        
        input("\nPresione Enter para continuar...")
    
    def simular_ciclo_celular(self):
        """Simula el ciclo celular y puntos de control"""
        self.mostrar_encabezado("SIMULACIÓN: CICLO CELULAR")
        
        fases = ["G1", "S", "G2", "M"]
        puntos_control = ["G1/S", "G2/M", "Metafase/Anafase"]
        
        print("Fases del ciclo celular:")
        for i, fase in enumerate(fases):
            print(f"  {i+1}. {fase}")
        
        print("\nPuntos de control (checkpoints):")
        for punto in puntos_control:
            print(f"  • {punto}")
        
        print("-" * 70)
        
        print("\nSimulación del avance del ciclo celular:")
        print("Presione Enter para avanzar a la siguiente fase...")
        input()
        
        for fase in fases:
            print(f"\nFASE {fase}:")
            
            if fase == "G1":
                print("  • Crecimiento celular")
                print("  • Síntesis de componentes")
                print("  • Checkpoint G1/S: verifica tamaño celular y nutrientes")
            
            elif fase == "S":
                print("  • Replicación del ADN")
                print("  • Síntesis de histonas")
                print("  • Duplicación de centrosomas")
            
            elif fase == "G2":
                print("  • Preparación para mitosis")
                print("  • Síntesis de componentes del huso")
                print("  • Checkpoint G2/M: verifica replicación completa")
            
            elif fase == "M":
                print("  • Mitosis: Profase, Metafase, Anafase, Telofase")
                print("  • Checkpoint metafase/anafase: verifica unión cromosómica")
                print("  • Citocinesis: división celular")
            
            input("  Presione Enter para continuar...")
        
        print("\n" + "=" * 70)
        print("Ciclo celular completado:")
        print("  1 célula madre → 2 células hijas")
        print("  ADN duplicado y segregado correctamente")
        
        input("\nPresione Enter para continuar...")

# ===========================================================================
# PROGRAMA PRINCIPAL
# ===========================================================================

def main():
    """Función principal del programa"""
    print("\n" + "=" * 70)
    print("SISTEMA DE ESTUDIO DE BIOLOGÍA CELULAR")
    print("Basado en el temario completo del curso 2025-2026")
    print("=" * 70 + "\n")
    
    try:
        # Iniciar interfaz
        interfaz = InterfazEstudio()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        print("El programa se cerrará.")

if __name__ == "__main__":
    main()