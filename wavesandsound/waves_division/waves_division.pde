float angleZ = radians(70);

void setup() {
  size(800, 400, P3D);
}

void draw() {
  background(255);
  translate(width / 2, height / 2);

  int gridSize = 10;
  int gridSpacing = 30;

  rotateZ(angleZ);

  for (int i = 0; i < gridSize; i++) {
    for (int j = 0; j < gridSize; j++) {
      float x = i * gridSpacing;
      float y = j * gridSpacing;

      beginShape();
      vertex(x, y, 0);
      vertex(x + gridSpacing, y, 0);
      vertex(x + gridSpacing, y + gridSpacing, 0);
      vertex(x, y + gridSpacing, 0);
      endShape(CLOSE);
    }
  }
}
