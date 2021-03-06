# From www.givingwhatwecan.org/scripts/includes/calculator.js
income_centiles=[
 [0, 0],
 [0.232, 60],
 [0.896, 120],
 [1.944, 180],
 [3.744, 240],
 [6.84, 300],
 [10.984, 360],
 [15.472, 420],
 [18.128, 456],
 [19.856, 480],
 [21.952, 510],
 [23.952, 540],
 [25.872, 570],
 [27.672, 600],
 [29.408, 630],
 [31.056, 660],
 [32.632, 690],
 [34.12, 720],
 [35.536, 750],
 [36.92, 780],
 [38.2, 810],
 [39.392, 840],
 [41.592, 900],
 [43.592, 960],
 [45.408, 1020],
 [47.04, 1080],
 [48.544, 1140],
 [49.928, 1200],
 [51.208, 1260],
 [52.392, 1320],
 [53.504, 1380],
 [54.536, 1440],
 [56.44, 1560],
 [58.112, 1680],
 [59.616, 1800],
 [61.6, 1980],
 [63.336, 2160],
 [65.328, 2400],
 [67.016, 2640],
 [68.464, 2880],
 [69.768, 3120],
 [70.832, 3360],
 [71.752, 3600],
 [72.736, 3900],
 [79, 6030],
 [80, 6431],
 [81, 6949],
 [82, 7549],
 [83, 8120],
 [84, 8826],
 [85, 9506],
 [86, 10402],
 [87, 11245],
 [88, 12164],
 [89, 13323],
 [90, 14447],
 [91, 15644],
 [92, 17093],
 [93, 18307],
 [94, 20383],
 [95, 22632],
 [96, 25401],
 [97, 29491],
 [98, 35472],
 [99, 46822],
 [99.9, 75894.28]]

def income_for_centile(centile):
  if centile <= income_centiles[0][0]:
    return income_centiles[0][1]
  for (c_a, i_a), (c_b, i_b) in zip(income_centiles, income_centiles[1:]):
    if c_a < centile <= c_b:
      centile_difference = c_b - c_a
      income_difference = i_b - i_a
      return i_a + ((centile - c_a) / centile_difference * income_difference)
  return -1

for step in range(1000):
  centile = step / 10.0
  print "%.2f\t%s" % (centile, income_for_centile(centile))
  
