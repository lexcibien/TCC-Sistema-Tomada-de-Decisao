/*
# Arquivo:

   UnicViewAD.h

# Projeto:

   UnicViewAD.lcm - Biblioteca Proculus em C

# Descrição:

   Esta biblioteca permite que um Arduino se comunique facilmente com o Displays
   Inteligentes Proculus, oferecendo um controle mais intuitivo e prático de todas
   as suas funções.

   Ela elimina a necessidade de um completo entendimento sobre todos os protocolos de
   comunicação e funcionamento interno do Display, abstraindo esses protocolos para
   pequenas funções que garantem facilidade e rapidez de uso.

# Autores:

   * Andreo de Freitas
   * Rafael Moura (revisão)

# Versão:

   1.0

# Licença:

   Copyright (c) 2020 Proculus Technologies Limited and Victor Vision LTDA

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in
   all copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
   THE SOFTWARE.

 */

#ifndef _PIC_GPD_Line_h
#define _PIC_GPD_Line_h

#include "lcm_gpd_area_c.h"

typedef struct gpd_line_parameters
{
   uint16_t vp;
   gpd_area_t area;
   uint16_t maximum_numbers_of_vertices;
   uint16_t color;
   uint16_t function_count;
} gpd_line_parameters_t;

   uint8_t lcm_gpd_line_begin(gpd_line_parameters_t* parameters);
   uint8_t lcm_gpd_line_set_function_count(gpd_line_parameters_t* parameters);
   uint8_t lcm_gpd_line_set_color(gpd_line_parameters_t* parameters);
   uint8_t lcm_gpd_line_clear(gpd_line_parameters_t* parameters);   
   uint8_t lcm_gpd_line_write(gpd_line_parameters_t* parameters, uint16_t x, uint16_t y, uint16_t vertex);
   uint8_t lcm_gpd_line_multiple_write(gpd_line_parameters_t* parameters, uint16_t* x, uint16_t* y, uint16_t length);

#endif
