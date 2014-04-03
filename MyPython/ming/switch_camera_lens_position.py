# -*- coding: utf-8 -*-
from Mobile import Mobile

if __name__ == '__main__':
    print 'start'

    m = Mobile('HYZPLVR48T6TS8LV')
    linearLayout = m.get_object(className='android.widget.LinearLayout', index=2)
    info_dict = m.get_info_of_object(linearLayout)
    print info_dict
    print info_dict['chileCount']
    chileCount = int(info_dict['chileCount']) - 1
    print chileCount
    btn = m.call(linearLayout, 'child', instance=chileCount, className='android.widget.ImageView')
    m.call(btn, 'click')

    print 'end'