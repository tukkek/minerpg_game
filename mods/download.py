#!/usr/bin/python3
# Used to download mods instead of having them in the repository
import os

MINERPG=True

def clone(url,branch='master'):
    os.system(f'git clone {url} --depth=1 --branch {branch}')

if MINERPG:
    clone('https://github.com/tukkek/minerpg.git')
clone('https://notabug.org/TenPlus1/mobs_redo')
clone('https://notabug.org/TenPlus1/mobs_monster')
clone('https://notabug.org/TenPlus1/mobs_animal')
clone('https://github.com/maikerumine/mobs_mc')
clone('https://github.com/D00Med/dmobs/')
clone('https://github.com/blert2112/mobs_water/')
clone('https://notabug.org/TenPlus1/lucky_block')
clone('https://github.com/minetest-mods/craftguide')
clone('https://github.com/e-y-e/MinetestAmbience.git',branch='fix_music')
clone('https://github.com/minetest-mods/anvil')
clone('https://github.com/minetest-mods/moretrees')
clone('https://github.com/minetest-mods/moreores')
