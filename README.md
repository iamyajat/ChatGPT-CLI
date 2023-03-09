# ChatGPT CLI

![image](https://user-images.githubusercontent.com/68477362/223910130-fce05d63-144b-4076-98da-cfe6cdaef584.png)

## Personas
The application comes with a bunch of preloaded personas. For example:
1. `school-teacher`
2. `nerd`
3. `sage`
4. `tech-bro`
5. `to-the-point`
6. `dev`
7. `romantic`

## Usage
```bash
$ python3 chatgpt.py --persona school-teacher
```

## Examples
1. **school-teacher**

    You: How are humans made?

    Assistant: Well, humans are made by something called "reproduction". When a mommy and a daddy love each other and want to have a baby, the daddy gives a tiny part of himself called a "sperm" to the mommy. The sperm meets up with a tiny egg cell that the mommy has, and together they start to grow inside the mommy's belly into a little baby. After a while, the baby gets big enough that it's ready to be born, and that's how humans come into the world!
    
2. **shakespeare**

    You: how are humans made?

    Assistant: Oh wondrous question, the very essence of creation itself! Humans, dear friend, are not simply made – they are woven together with the threads of ambition, joy, sorrow, and wonder. Like a tapestry on a loom, each person is unique – a masterpiece crafted by the Master Designer. Indeed, we are formed from the dust of the earth but also imbued with a divine spark, a slice of celestial light that sets us apart from all other creatures. The process of shaping a human being is like the creation of a great work of literature – carefully crafted, beautifully nuanced, and imbued with a depth of meaning that extends far beyond the mere sum of its parts. So, my dear friend, we are not simply made, but rather, we are formed with the very essence of the universe itself.  

3. **to-the-point**

    You: how are humans made?

    Assistant: Humans are made when a sperm from a male joins with an egg from a female, which then grows into a fetus inside the mother's uterus for nine months before being born.

4. **nerd**

    You: how are humans made?

    Assistant:

    Humans are complex organisms that are made up of millions of cells of different types, each with a specific function. The process of making a human being involves several stages, starting with fertilization and ending with the birth of a baby.

    Fertilization is the process by which a sperm cell from the male and an egg cell from the female combine to form a zygote, which is the first stage of a human embryo. The sperm cells are produced in the testes of the male and are released during ejaculation. The egg cells, on the other hand, are produced in the ovaries of the female and are released during ovulation.

    Once the sperm and egg cells combine, the zygote begins to divide rapidly through a process known as mitosis. This process results in the formation of a blastocyst, which is a hollow ball of cells that is implanted in the lining of the uterus. Over the next few weeks, the cells continue to divide and differentiate into different types of cells, such as muscle cells, nerve cells, and blood cells.

    As the embryo grows, it develops a head, a body, and limbs. The head contains the brain and the sensory organs, such as the eyes, ears, nose, and mouth. The body contains the organs, such as the heart, lungs, liver, and kidneys, which are responsible for maintaining the body's functions. The limbs are used for movement and manipulation.

    During the third trimester of pregnancy, the baby's organs mature, and the body becomes prepared for life outside of the womb. When the baby reaches full term, it is ready for delivery. The process of giving birth involves the contraction of the uterus, which pushes the baby out of the birth canal and into the world.

    In summary, the process of making a human being involves fertilization, growth, and development of the embryo inside the uterus, and the final stages of preparation for birth. This is a complex process that involves the interaction of many systems and processes, and it is still the subject of ongoing research and study.       

5. **sage**
 
    You: how are humans made?

    Assistant: Humans, like all living things, are the result of a process called reproduction. It begins with a man and a woman who have special cells in their bodies called sperm and eggs, respectively. When a sperm from the man's body meets an egg from the woman's body, they join together to form a new cell called a zygote.

    The zygote then divides and grows into an embryo, which eventually develops into a fetus, and finally a baby. During this process, the baby's organs, limbs, and other body parts develop and take shape.

    It's a bit like baking a cake. The sperm and egg are like the ingredients, and when they come together, they create the "batter" - the zygote. Just like a batter needs time to rise and bake in the oven, the zygote needs time to develop in the woman's womb. And just like a cake takes shape as it bakes, the baby takes shape as it grows and develops in the womb.

    Overall, the process of making a human is a truly miraculous and complex one, but it all starts with a man and a woman, and the magical way their bodies come together to create new life.


6. **tech-bro**

    You: how are humans made?

    Assistant: Well, humans are the result of a complex biological process involving DNA replication and cellular differentiation, facilitated by various technological advancements in fields such as genomics, proteomics, and biotechnology. Additionally, factors such as epigenetics and environmental influences play a significant role in shaping human development, making it a truly multi-disciplinary endeavor requiring expertise in fields such as machine learning, neuroscience, and bioinformatics to fully understand.

7. **romantic**

    You: how are humans made?

    Assistant: Oh, my dear summer breeze, the creation of humans is a mystical and awe-inspiring phenomenon. Just like the finest work of art, every person is delicately crafted and uniquely endowed with a soul that sets them apart from anyone else.

    Some believe that humans were molded by the divine hands of a higher power, while others say that we emerged from the majesty of the universe's cosmic energy. Regardless of where one believes we originated, we all possess an inexplicable essence that illuminates the world.

    Perhaps, humans are like flowers that sprout from the earth, each with their distinctive hue and scent, or maybe we are like the stars twinkling brilliantly in the vast expanse of the night sky. Whatever the case may be, there is no doubt that we are extraordinary beings, formed from a blend of magic and wonder.

    In the end, the creation of humanity remains one of life's greatest mysteries, but what we do know is that we were made to love, to create, and to cherish each other's company - and that is what makes our existence truly remarkable.
    
8. **dev**

    You: how are humans made?

    Assistant: Humans are made through a process called sexual reproduction, which involves the fusion of a sperm cell from the father with an egg cell from the mother. This process takes place during sexual intercourse, where the sperm is ejaculated from the man's penis into the woman's vagina, travels up to the uterus, and fertilizes the egg if it is present.

    Once the egg is fertilized, it starts to divide and forms a ball of cells known as a zygote, which eventually implants itself in the lining of the uterus. Over time, the zygote develops into an embryo, which then grows and develops into a fetus over the course of approximately nine months.

    During this time, the fetus grows and develops various body systems, such as the nervous system, cardiovascular system, and respiratory system. It receives nutrients and oxygen through the placenta, which is attached to the lining of the uterus and provides a connection between the mother and the developing fetus.

    Ultimately, after approximately 40 weeks of gestation, the fetus is fully developed and ready to be born. The mother goes into labor, during which the fetus is pushed out of the uterus and into the world, where it takes its first breath and begins its journey through life.

    Here’s some simple Python code that shows how an egg and sperm can combine to form a zygote:
    ```
    class Egg:
      def __init__(self):
        self.fertilized = False

      def fertilize(self):
        self.fertilized = True

      def is_fertilized(self):
        return self.fertilized

    class Sperm:
      def __init__(self):
        self.fertilized = False

      def fertilize(self, egg):
        egg.fertilize()
        self.fertilized = True

      def is_fertilized(self):
        return self.fertilized

    egg = Egg()
    sperm = Sperm()
    sperm.fertilize(egg)

    if egg.is_fertilized():
      print("The egg has been fertilized!")
    else:
      print("The egg has not been fertilized yet.")
    ```
    

