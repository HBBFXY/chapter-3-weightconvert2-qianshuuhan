weight = float(input('请输入你当前在地球上的体重:')
a = 0.5
moon = 0.165
print('未来10年地球和月球体重变化:')
for year in range(1,11):
    earth_weight = weight + a * year
    moon_weight = earth_weight * 0.165
    print(f'第{year}年:地球上的体重{earth_weight:.2f}kg,月球上的体重{moon_weight:.2f}kg')
