/**
 * Distance 2D. 
 * 
 * Move the mouse across the image to obscure and reveal the matrix.  
 * Measures the distance from the mouse to each square and sets the
 * size proportionally. 
 */
 
float max_distance;

void setup() {
  size(1340, 1060); 
  noStroke();
  max_distance = dist(0, 0, width, height);
}

void draw() {
  background  (193,227,179);

  for(int i = 0; i <= width; i += 30) {
    for(int j = 0; j <= height; j += 30) {
      float size = dist(mouseX, mouseY, i, j);
      size = size/max_distance * 66;
      fill(214,113,203);
      ellipse(i, j, size, size);
    }
  }
}
