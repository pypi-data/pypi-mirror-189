======================
Test Cases from Issues
======================

Issues #6: Harmonize horizontal spacing lists
=============================================

:Link: https://gitlab.com/anatas_ch/pyl_mrtoolstheme/-/issues/6
:Fixed: 0.5.0

.. code-block:: rest
    :caption: Test Case

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua.

    #. first entry
    #. second entry

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua.

    - first entry
    - second entry

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua.

    first entry
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua.
    second entry
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
    dolore magna aliqua.

---------------------------------------------------------------------------------------------------------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua.

#. first entry
#. second entry

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua.

- first entry
- second entry

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua.

first entry
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua.
second entry
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua.

Issues #5: Spacing around table captions
========================================

:Link: https://gitlab.com/anatas_ch/pyl_mrtoolstheme/-/issues/4
:Fixed: 0.5.0

.. code-block:: rest
    :caption: Test Case

    Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica,
    sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation
    e li plu commun vocabules. Li Europan lingues es membres del sam familie.

    .. table:: The test table for the caption formatting.
        :name: tab-issues-5

        ======= ======= ======= ======= =======
        Test A  Test B  Test C  Test D  Test E
        ======= ======= ======= ======= =======
        123     345     951         951 584
        456     789     9587    125     6548
        ======= ======= ======= ======= =======

    Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica,
    sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation
    e li plu commun vocabules. See :numref:`tab-issues-5`.


---------------------------------------------------------------------------------------------------------------

Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica,
sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation
e li plu commun vocabules. Li Europan lingues es membres del sam familie.

.. table:: The test table for the caption formatting.
    :name: tab-issues-5

    ======= ======= ======= ======= =======
    Test A  Test B  Test C  Test D  Test E
    ======= ======= ======= ======= =======
    123     345     951         951 584
    456     789     9587    125     6548
    ======= ======= ======= ======= =======

Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica,
sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation
e li plu commun vocabules. See :numref:`tab-issues-5`.


Issues #4: Spacing around figure caption
========================================

:Link: https://gitlab.com/anatas_ch/pyl_mrtoolstheme/-/issues/4
:Fixed: 0.5.0

.. code-block:: rest
    :caption: Test Case

    .. figure:: _static/logo_toolstheme.png

        The project logo.

        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo
        ligula eget  dolor. Aenean massa.

        Cum sociis natoque penatibus et magnis dis parturient montes, nascetur
        ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium
        quis, sem. Nulla consequat massa quis enim.

---------------------------------------------------------------------------------------------------------------

.. figure:: _static/logo_toolstheme.png

    The project logo.

    Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo
    ligula eget  dolor. Aenean massa.

    Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus
    mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla
    consequat massa quis enim.


Issues #3: Numbered lists in admonitions
========================================

:Link: https://gitlab.com/anatas_ch/pyl_mrtoolstheme/-/issues/3
:Fixed: 0.5.0

.. code-block:: rest
    :caption: Test Case

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
    dolore magna aliqua.

    #. first entry
    #. second entry

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
    dolore magna aliqua.

    - first entry

      #. first entry
      #. second entry

    - second entry

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
    dolore magna aliqua.


    .. admonition:: Numbered lists in admonitions

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
        dolore magna aliqua.

        #. first entry

           #. first entry

              #. first entry
              #. second entry

           #. second entry

        #. second entry

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
        dolore magna aliqua.

        #. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
           et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
           tempor incididunt ut labore et dolore magna aliqua.
        #. Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, weil er Schmerz ist,
           es sei denn, es kommt zu zufälligen Umständen, in denen Mühen und Schmerz ihm große Freude bereiten
           können.

        a. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
           et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
           tempor incididunt ut labore et dolore magna aliqua.

           #. Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, weil er Schmerz
              ist, es sei denn, es kommt zu zufälligen Umständen, in denen Mühen und Schmerz ihm große Freude
              bereiten können.

        Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica,
        sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li
        pronunciation e li plu commun vocabules

    Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, weil er Schmerz ist, es sei
    denn, es kommt zu zufälligen Umständen, in denen Mühen und Schmerz ihm große Freude bereiten können. Um ein
    triviales Beispiel zu nehmen, wer von uns unterzieht sich je anstrengender körperlicher Betätigung, außer um
    Vorteile daraus zu ziehen?

---------------------------------------------------------------------------------------------------------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua.

#. first entry
#. second entry

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua.

- first entry

  #. first entry
  #. second entry

- second entry

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua.


.. admonition:: Numbered lists in admonitions

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
    dolore magna aliqua.

    #. first entry

       #. first entry

          #. first entry
          #. second entry

       #. second entry

    #. second entry

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
    dolore magna aliqua.

    #. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
       dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
       incididunt ut labore et dolore magna aliqua.
    #. Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, weil er Schmerz ist, es
       sei denn, es kommt zu zufälligen Umständen, in denen Mühen und Schmerz ihm große Freude bereiten können.

       a. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
          dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
          incididunt ut labore et dolore magna aliqua.

          #. Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, weil er Schmerz ist, es
             sei denn, es kommt zu zufälligen Umständen, in denen Mühen und Schmerz ihm große Freude bereiten können.

    Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica,
    sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation
    e li plu commun vocabules

Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, weil er Schmerz ist, es sei
denn, es kommt zu zufälligen Umständen, in denen Mühen und Schmerz ihm große Freude bereiten können. Um ein
triviales Beispiel zu nehmen, wer von uns unterzieht sich je anstrengender körperlicher Betätigung, außer um
Vorteile daraus zu ziehen?


Issues #2: Text as code formatted in ``code-block`` ``caption``
===============================================================

:Link: https://gitlab.com/anatas_ch/pyl_mrtoolstheme/-/issues/2
:Fixed: 0.3.0

.. code-block:: rest
    :caption: Test Case

    .. code-block:: json
       :caption: ``Some as code formated text`` and some normal text!

       {
           "testcase": "issues 2"
       }

---------------------------------------------------------------------------------------------------------------

.. code-block:: json
   :caption: ``Some as code formated text`` and some normal text!

   {
       "testcase": "issues 2"
   }


Issues #1: ``code-block`` in ``admonition``
===========================================

:Link: https://gitlab.com/anatas_ch/pyl_mrtoolstheme/-/issues/1
:Fixed: 0.2.0

.. code-block:: rest
    :caption: Test Case

    .. Note:: Never use ``l``, ``O``, or ``I`` single letter names as these can be mistaken
              for ``1`` and ``0``, depending on typeface:

        .. code-block:: python
            :caption: Python

            O = 2    # This may look like you're trying to reassign 2 to zero

---------------------------------------------------------------------------------------------------------------

.. Note:: Never use ``l``, ``O``, or ``I`` single letter names as these can be mistaken for ``1`` and ``0``,
          depending on typeface:

          .. code-block:: python
              :caption: Python

              O = 2    # This may look like you're trying to reassign 2 to zero
