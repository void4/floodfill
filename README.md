## Flood fill

`pip install -r requirements.txt`

Maybe use some of these as well:

```python
cd anim/
# Resize images
mogrify -resize 640x480 *.jpg
# Add leading zeroes to file names
ls | awk '/^([0-9]+)\.jpg$/ { printf("%s %05d.jpg\n", $0, $1) }' | xargs -n2 mv
# Convert to gif
#convert -resize 25% -delay 20 -loop 0  *.jpg ../animated.gif
# Convert to webm
ffmpeg -framerate 25 -f image2 -i %05d.jpg -c:v libvpx-vp9 -pix_fmt yuva420p ../output.webm

```
