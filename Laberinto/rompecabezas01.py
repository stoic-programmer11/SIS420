{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "id": "VQ8ZQGc78VHX"
      },
      "outputs": [],
      "source": [
        "estado_inicial = [3, 2, 0, 1]\n",
        "estado_objetivo = [0, 1, 2, 3]\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def generar_nuevos_estados(estado_inicial):\n",
        "  nuevo_estado_1 = [estado_inicial[1], estado_inicial[0], estado_inicial[2], estado_inicial[3]]\n",
        "  nuevo_estado_2 = [estado_inicial[0], estado_inicial[2], estado_inicial[1], estado_inicial[3]]\n",
        "  nuevo_estado_3 = [estado_inicial[0], estado_inicial[1], estado_inicial[3], estado_inicial[2]]\n",
        "\n",
        "  nuevos_estados = []\n",
        "  nuevos_estados.append(nuevo_estado_1)\n",
        "  nuevos_estados.append(nuevo_estado_2)\n",
        "  nuevos_estados.append(nuevo_estado_3)\n",
        "  return nuevos_estados"
      ],
      "metadata": {
        "id": "fxWaznIs8v4R"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "estados_frontera = []\n",
        "estados_revisados = []\n",
        "estados_frontera.extend([estado_inicial])\n",
        "estado_actual = estado_inicial\n",
        "\n",
        "while(estado_actual != estado_objetivo and len(estados_frontera) > 0):\n",
        "  aux_estados = generar_nuevos_estados(estado_actual)\n",
        "  estados_frontera.extend(aux_estados)\n",
        "  estados_revisados.append(estado_actual)\n",
        "  print(\"ESTADOS FRONTERA\")\n",
        "  print(estados_frontera)\n",
        "  estado_actual = estados_frontera.pop(0)\n",
        "  while estado_actual in estados_revisados:\n",
        "    estado_actual = estados_frontera.pop(0)\n",
        "  \n",
        "  \n",
        "  print(\"ESTADOS REVISADOS\")\n",
        "  print(estados_revisados)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tN97lOLv9HL8",
        "outputId": "8e9fd3a0-bb54-4743-bd7e-f4ae4e546d9a"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ESTADOS FRONTERA\n",
            "[[3, 0, 2, 1], [3, 2, 1, 0]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1]]\n",
            "ESTADOS FRONTERA\n",
            "[[3, 2, 1, 0], [3, 2, 0, 1], [2, 0, 3, 1], [2, 3, 1, 0]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1]]\n",
            "ESTADOS FRONTERA\n",
            "[[3, 2, 0, 1], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 2, 0, 1], [3, 0, 1, 2]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1]]\n",
            "ESTADOS FRONTERA\n",
            "[[2, 3, 1, 0], [0, 3, 2, 1], [3, 2, 0, 1], [3, 0, 1, 2], [2, 3, 1, 0], [3, 1, 2, 0], [3, 2, 0, 1]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0]]\n",
            "ESTADOS FRONTERA\n",
            "[[0, 3, 2, 1], [3, 2, 0, 1], [3, 0, 1, 2], [2, 3, 1, 0], [3, 1, 2, 0], [3, 2, 0, 1], [0, 2, 3, 1], [2, 3, 0, 1], [2, 0, 1, 3]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1]]\n",
            "ESTADOS FRONTERA\n",
            "[[3, 2, 0, 1], [3, 0, 1, 2], [2, 3, 1, 0], [3, 1, 2, 0], [3, 2, 0, 1], [0, 2, 3, 1], [2, 3, 0, 1], [2, 0, 1, 3], [3, 2, 1, 0], [2, 1, 3, 0], [2, 3, 0, 1]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0]]\n",
            "ESTADOS FRONTERA\n",
            "[[2, 3, 1, 0], [3, 1, 2, 0], [3, 2, 0, 1], [0, 2, 3, 1], [2, 3, 0, 1], [2, 0, 1, 3], [3, 2, 1, 0], [2, 1, 3, 0], [2, 3, 0, 1], [3, 0, 2, 1], [0, 2, 3, 1], [0, 3, 1, 2]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1]]\n",
            "ESTADOS FRONTERA\n",
            "[[3, 2, 0, 1], [0, 2, 3, 1], [2, 3, 0, 1], [2, 0, 1, 3], [3, 2, 1, 0], [2, 1, 3, 0], [2, 3, 0, 1], [3, 0, 2, 1], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 1, 2], [3, 1, 0, 2], [3, 0, 2, 1]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2]]\n",
            "ESTADOS FRONTERA\n",
            "[[2, 3, 0, 1], [2, 0, 1, 3], [3, 2, 1, 0], [2, 1, 3, 0], [2, 3, 0, 1], [3, 0, 2, 1], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 1, 2], [3, 1, 0, 2], [3, 0, 2, 1], [1, 3, 2, 0], [3, 2, 1, 0], [3, 1, 0, 2]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0]]\n",
            "ESTADOS FRONTERA\n",
            "[[3, 2, 1, 0], [2, 1, 3, 0], [2, 3, 0, 1], [3, 0, 2, 1], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 1, 2], [3, 1, 0, 2], [3, 0, 2, 1], [1, 3, 2, 0], [3, 2, 1, 0], [3, 1, 0, 2], [2, 0, 3, 1], [0, 3, 2, 1], [0, 2, 1, 3]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0], [0, 2, 3, 1]]\n",
            "ESTADOS FRONTERA\n",
            "[[2, 3, 0, 1], [3, 0, 2, 1], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 1, 2], [3, 1, 0, 2], [3, 0, 2, 1], [1, 3, 2, 0], [3, 2, 1, 0], [3, 1, 0, 2], [2, 0, 3, 1], [0, 3, 2, 1], [0, 2, 1, 3], [0, 2, 1, 3], [2, 1, 0, 3], [2, 0, 3, 1]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0], [0, 2, 3, 1], [2, 0, 1, 3]]\n",
            "ESTADOS FRONTERA\n",
            "[[0, 3, 1, 2], [3, 1, 0, 2], [3, 0, 2, 1], [1, 3, 2, 0], [3, 2, 1, 0], [3, 1, 0, 2], [2, 0, 3, 1], [0, 3, 2, 1], [0, 2, 1, 3], [0, 2, 1, 3], [2, 1, 0, 3], [2, 0, 3, 1], [1, 2, 3, 0], [2, 3, 1, 0], [2, 1, 0, 3]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0], [0, 2, 3, 1], [2, 0, 1, 3], [2, 1, 3, 0]]\n",
            "ESTADOS FRONTERA\n",
            "[[3, 0, 2, 1], [1, 3, 2, 0], [3, 2, 1, 0], [3, 1, 0, 2], [2, 0, 3, 1], [0, 3, 2, 1], [0, 2, 1, 3], [0, 2, 1, 3], [2, 1, 0, 3], [2, 0, 3, 1], [1, 2, 3, 0], [2, 3, 1, 0], [2, 1, 0, 3], [3, 0, 1, 2], [0, 1, 3, 2], [0, 3, 2, 1]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0], [0, 2, 3, 1], [2, 0, 1, 3], [2, 1, 3, 0], [0, 3, 1, 2]]\n",
            "ESTADOS FRONTERA\n",
            "[[3, 2, 1, 0], [3, 1, 0, 2], [2, 0, 3, 1], [0, 3, 2, 1], [0, 2, 1, 3], [0, 2, 1, 3], [2, 1, 0, 3], [2, 0, 3, 1], [1, 2, 3, 0], [2, 3, 1, 0], [2, 1, 0, 3], [3, 0, 1, 2], [0, 1, 3, 2], [0, 3, 2, 1], [1, 3, 0, 2], [3, 0, 1, 2], [3, 1, 2, 0]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0], [0, 2, 3, 1], [2, 0, 1, 3], [2, 1, 3, 0], [0, 3, 1, 2], [3, 1, 0, 2]]\n",
            "ESTADOS FRONTERA\n",
            "[[0, 2, 1, 3], [2, 1, 0, 3], [2, 0, 3, 1], [1, 2, 3, 0], [2, 3, 1, 0], [2, 1, 0, 3], [3, 0, 1, 2], [0, 1, 3, 2], [0, 3, 2, 1], [1, 3, 0, 2], [3, 0, 1, 2], [3, 1, 2, 0], [3, 1, 2, 0], [1, 2, 3, 0], [1, 3, 0, 2]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0], [0, 2, 3, 1], [2, 0, 1, 3], [2, 1, 3, 0], [0, 3, 1, 2], [3, 1, 0, 2], [1, 3, 2, 0]]\n",
            "ESTADOS FRONTERA\n",
            "[[2, 0, 3, 1], [1, 2, 3, 0], [2, 3, 1, 0], [2, 1, 0, 3], [3, 0, 1, 2], [0, 1, 3, 2], [0, 3, 2, 1], [1, 3, 0, 2], [3, 0, 1, 2], [3, 1, 2, 0], [3, 1, 2, 0], [1, 2, 3, 0], [1, 3, 0, 2], [2, 0, 1, 3], [0, 1, 2, 3], [0, 2, 3, 1]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0], [0, 2, 3, 1], [2, 0, 1, 3], [2, 1, 3, 0], [0, 3, 1, 2], [3, 1, 0, 2], [1, 3, 2, 0], [0, 2, 1, 3]]\n",
            "ESTADOS FRONTERA\n",
            "[[2, 3, 1, 0], [2, 1, 0, 3], [3, 0, 1, 2], [0, 1, 3, 2], [0, 3, 2, 1], [1, 3, 0, 2], [3, 0, 1, 2], [3, 1, 2, 0], [3, 1, 2, 0], [1, 2, 3, 0], [1, 3, 0, 2], [2, 0, 1, 3], [0, 1, 2, 3], [0, 2, 3, 1], [1, 2, 0, 3], [2, 0, 1, 3], [2, 1, 3, 0]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0], [0, 2, 3, 1], [2, 0, 1, 3], [2, 1, 3, 0], [0, 3, 1, 2], [3, 1, 0, 2], [1, 3, 2, 0], [0, 2, 1, 3], [2, 1, 0, 3]]\n",
            "ESTADOS FRONTERA\n",
            "[[0, 3, 2, 1], [1, 3, 0, 2], [3, 0, 1, 2], [3, 1, 2, 0], [3, 1, 2, 0], [1, 2, 3, 0], [1, 3, 0, 2], [2, 0, 1, 3], [0, 1, 2, 3], [0, 2, 3, 1], [1, 2, 0, 3], [2, 0, 1, 3], [2, 1, 3, 0], [2, 1, 3, 0], [1, 3, 2, 0], [1, 2, 0, 3]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0], [0, 2, 3, 1], [2, 0, 1, 3], [2, 1, 3, 0], [0, 3, 1, 2], [3, 1, 0, 2], [1, 3, 2, 0], [0, 2, 1, 3], [2, 1, 0, 3], [1, 2, 3, 0]]\n",
            "ESTADOS FRONTERA\n",
            "[[3, 0, 1, 2], [3, 1, 2, 0], [3, 1, 2, 0], [1, 2, 3, 0], [1, 3, 0, 2], [2, 0, 1, 3], [0, 1, 2, 3], [0, 2, 3, 1], [1, 2, 0, 3], [2, 0, 1, 3], [2, 1, 3, 0], [2, 1, 3, 0], [1, 3, 2, 0], [1, 2, 0, 3], [1, 0, 3, 2], [0, 3, 1, 2], [0, 1, 2, 3]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0], [0, 2, 3, 1], [2, 0, 1, 3], [2, 1, 3, 0], [0, 3, 1, 2], [3, 1, 0, 2], [1, 3, 2, 0], [0, 2, 1, 3], [2, 1, 0, 3], [1, 2, 3, 0], [0, 1, 3, 2]]\n",
            "ESTADOS FRONTERA\n",
            "[[0, 2, 3, 1], [1, 2, 0, 3], [2, 0, 1, 3], [2, 1, 3, 0], [2, 1, 3, 0], [1, 3, 2, 0], [1, 2, 0, 3], [1, 0, 3, 2], [0, 3, 1, 2], [0, 1, 2, 3], [3, 1, 0, 2], [1, 0, 3, 2], [1, 3, 2, 0]]\n",
            "ESTADOS REVISADOS\n",
            "[[3, 2, 0, 1], [2, 3, 0, 1], [3, 0, 2, 1], [3, 2, 1, 0], [2, 0, 3, 1], [2, 3, 1, 0], [0, 3, 2, 1], [3, 0, 1, 2], [3, 1, 2, 0], [0, 2, 3, 1], [2, 0, 1, 3], [2, 1, 3, 0], [0, 3, 1, 2], [3, 1, 0, 2], [1, 3, 2, 0], [0, 2, 1, 3], [2, 1, 0, 3], [1, 2, 3, 0], [0, 1, 3, 2], [1, 3, 0, 2]]\n"
          ]
        }
      ]
    }
  ]
}