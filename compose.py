import content.en_us
#import content.zh_cn
import template.process

template.process.compose(content.en_us.content, "index.html")
#template.process.compose(content.zh_cn.content, "zh_cn.html")