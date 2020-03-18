
let cols = 20;
let rows = 20;
let size = 30;

let change_x = -1;
let change_y = 0;

let wished_lenght = 3;

let apples = [
  [10, 10], 
]

var snake = [
  [parseInt(cols / 2), parseInt(rows / 2)],
  [parseInt(cols / 2 + 1), parseInt(rows / 2)],
  [parseInt(cols / 2 + 2), parseInt(rows / 2)]
];

function setup() {
  //canvas
  createCanvas(cols*size, rows*size);
  frameRate(10)
}

function draw() {

  background(100);
  stroke(255);

  // for (let i = 0; i < snake.length; i ++) {

  //   fill(255);
  //   rect(snake[i][0] * size, snake[i][1] *  size, size, size)

  // }
  
  //Draw grid snake, and apple  -------------------------------------------------->
  for (let x = 0; x < cols; x++) {
    for (let y = 0; y < rows; y++) {

      let in_apple = 0;
      let in_snake = 0;
      let head = 0;
      let tail = 0;

      for (let i = 0; i < snake.length; i++) {
        if (snake[i][0] == x && snake[i][1] == y) {
          in_snake = 1;
          if (i == 0) {
            head = 1;
          }
        }
      }

      for (let i = 0; i < apples.length; i++) {
        if (apples[i][0] == x && apples[i][1] == y) {
          in_apple = 1;
        }
      }

      
      if (in_snake) {
        fill(0,0,map(wished_lenght,0,cols*rows,200,255));
      } else if (in_apple){
        fill(255,0,0)
      }  else {
        if ((x + y) / 2 % 2 == 0) {
          fill(179,219,104);
        } else {
          fill(164,198,95);

        }
        
      }

      rect(x * size, y *  size, size, size)

      if (head) {
        fill(0)
        print("eye");
        ellipse(x * size + size / 2,y * size + size / 2, 10);
        fill(255);
      }

      fill(0)
      textSize(32)
      text(wished_lenght, 2 * size, 2 * size)

    }

  }

  //Update snake --------------------------------------------------------->
  let head = snake[0]
  let new_head = [head[0] + change_x, head[1] + change_y];
  let in_snake = 1;
  let valid_head = 1;

  for (let i = 0; i < snake.length; i++) {
    for (let j = 0; j < apples.length; j ++) {
      if (snake[i][0] == apples[j][0] && snake[i][1] == apples[j][1]) {
        wished_lenght += 1;
        console.log("killed apple");
        apples.splice(apples.indexOf(j), 1)
        apples.push([parseInt(random(0,cols)), parseInt(random(0,rows))])
      }
    }
  }

  for (let i = 0; i < snake.length; i++ ) {
    if ((new_head[0] == snake[i][0] && new_head[1] == snake[i][1]) || (new_head[0] < 0 || new_head[0] > cols) || (new_head[1] < 0 || new_head[1] > rows)) {
      valid_head = 0;
    }
  }

  if (valid_head) {
    //length = snake.push(new_head);
    console.log(snake.length)

    //Add head to the front of the array
    snake.unshift(new_head);
    
    if (snake.length > wished_lenght) {
      //Remove last element from array
      snake.pop();
    }
  } else {
    console.log("invalid head")
    location.reload();
  }

  // -------------------------------------------------------------------->
  
}


function keyPressed() {

  change_x = 0;
  change_y = 0;

  if (keyCode == UP_ARROW) {
    change_y = -1;
  } else if (keyCode == DOWN_ARROW) {
    change_y = 1;
  } else if (keyCode == RIGHT_ARROW) {
    change_x = 1;
  } else if (keyCode   == LEFT_ARROW) {
    change_x = -1;
  }
}