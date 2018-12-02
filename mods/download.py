#!/usr/bin/python3
# Used to download mods instead of having them in the repository
import os

def clone(url,branch='master',after=False):
  if os.system(f'git clone {url} --depth=1 --branch {branch}')!=0:
    return False
  if after!=False:
    os.system(after)
  return True

clone('https://github.com/tukkek/minerpg.git')

if clone('https://github.com/minetest/minetest_game/'):
  os.system('rm -r minetest_game/mods/screwdriver/')
  os.system('mv minetest_game/mods/* .')
  os.system('rm -rf minetest_game/')
  os.system('touch minetest_game')

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
clone('https://github.com/minetest-mods/biome_lib')
clone('https://github.com/paramat/snowdrift.git')
clone('https://github.com/minetest-mods/torches')

clone('https://bitbucket.org/kingarthursteam/teleporter.git')
clone('https://bitbucket.org/adrido/db.git')

clone('https://repo.or.cz/minetest_treasurer.git',after='mv minetest_treasurer treasurer')
clone('https://repo.or.cz/tsm_mines.git')
clone('https://repo.or.cz/minetest_pyramids/tsm_pyramids.git')
