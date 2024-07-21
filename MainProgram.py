import os
import shutil

file_first_path = "Map1"
file_second_path = "Map2"
new_directory = "NewFolder"

dirs_paths_map1, dirs_paths_map2 = [], []

for file_name in os.listdir(file_first_path):
     dirs_paths_map1.append( os.path.join(file_first_path, file_name ))
     dirs_paths_map2.append( os.path.join(file_second_path, file_name ))

def copy_waypoints(map1, map2):
     if not(os.path.isdir(f'{new_directory}\\waypoints')):
          os.mkdir(f'{new_directory}\\waypoints')
     waypoints_name_map1, waypoints_name_map2 = [], []
     for waypoints_name in os.listdir(map1):
          waypoints_name_map1.append( os.path.join(map1, waypoints_name ))

     for waypoints_name in os.listdir(map2):
          waypoints_name_map2.append( os.path.join(map2, waypoints_name ))

     list_for_new_folder = waypoints_name_map1 + waypoints_name_map2
     list_for_new_folder = list(set(list_for_new_folder))

     for count_file in range(len(list_for_new_folder)):
         shutil.copy2(list_for_new_folder[count_file], f"{new_directory}\\waypoints")



def copy_dimension(map1, map2, location):
     if not(os.path.isdir(f'{new_directory}\\{location}')):
          os.mkdir(f'{new_directory}\\{location}')

     dirs_paths_map1, dirs_paths_map2 = {}, {}
     for dir_name in os.listdir(map1):
          dirs_paths_map1[os.path.splitext(os.path.basename(dir_name))[0]] = os.path.join(map1 , dir_name)
     for dir_name in os.listdir(map2):
          dirs_paths_map2[os.path.splitext(os.path.basename(dir_name))[0]] = os.path.join(map2 , dir_name)

     for layer in os.listdir(map1):
          if not(layer in dirs_paths_map2):
               if not(os.path.isdir(f'{new_directory}\\{location}\\{layer}')):
                    shutil.copytree(f'{dirs_paths_map1[layer]}', f'{new_directory}\\{location}\\{layer}')
          else:
               if not(os.path.isdir(f'{new_directory}\\{location}\\{layer}')):
                    os.mkdir(f'{new_directory}\\{location}\\{layer}')
               for layer_dirs in os.listdir(dirs_paths_map1[layer]):
                    if layer_dirs == 'cache':
                         if not(os.path.isdir(f'{new_directory}\\{location}\\{layer}\\cache')):
                              os.mkdir(f'{new_directory}\\{location}\\{layer}\\cache')
                         for cache_file in os.listdir(dirs_paths_map1[layer] + f"\\{layer_dirs}"):
                              if cache_file in os.listdir(dirs_paths_map2[layer] + f"\\{layer_dirs}"):
                                   if os.path.getctime(dirs_paths_map1[layer] + f"\\cache\\{cache_file}") > os.path.getctime(dirs_paths_map2[layer] + f"\\cache\\{cache_file}"):
                                        copy_file = dirs_paths_map1[layer] + f"\\cache\\{cache_file}"
                                   else:
                                        copy_file = dirs_paths_map2[layer] + f"\\cache\\{cache_file}"
                                   shutil.copy2(copy_file, f'{new_directory}\\{location}\\{layer}\\{layer_dirs}')
                              else:
                                   shutil.copy2(dirs_paths_map1[layer] + f"\\{layer_dirs}\\{cache_file}", f'{new_directory}\\{location}\\{layer}\\{layer_dirs}')
                    else:
                         if layer_dirs in os.listdir(dirs_paths_map2[layer]):
                              if os.path.getctime(dirs_paths_map1[layer] + f"\\{layer_dirs}") > os.path.getctime(dirs_paths_map2[layer] + f"\\{layer_dirs}"):
                                   copy_file = dirs_paths_map1[layer] + f"\\{layer_dirs}"
                              else:
                                   copy_file = dirs_paths_map2[layer] + f"\\{layer_dirs}"
                              shutil.copy2(copy_file, f'{new_directory}\\{location}\\{layer}')
                         else:
                              shutil.copy2(f'{dirs_paths_map1[layer]}\\{layer_dirs}', f'{new_directory}\\{location}\\{layer}')

     for layer in os.listdir(map2):
          if not(layer in dirs_paths_map1):
               if not(os.path.isdir(f'{new_directory}\\{location}\\{layer}')):
                    shutil.copytree(f'{dirs_paths_map2[layer]}', f'{new_directory}\\{location}\\{layer}')
          else:
               if not(os.path.isdir(f'{new_directory}\\{location}\\{layer}')):
                    os.mkdir(f'{new_directory}\\{location}\\{layer}')
               for layer_dirs in os.listdir(dirs_paths_map2[layer]):
                    if layer_dirs == 'cache':
                         if not(os.path.isdir(f'{new_directory}\\{location}\\{layer}\\cache')):
                              os.mkdir(f'{new_directory}\\{location}\\{layer}\\cache')
                         for cache_file in os.listdir(dirs_paths_map2[layer] + f"\\{layer_dirs}"):
                              if not(cache_file in os.listdir(f'{new_directory}\\{location}\\{layer}\\{layer_dirs}')):
                                   shutil.copy2(dirs_paths_map2[layer] + f"\\{layer_dirs}\\{cache_file}", f'{new_directory}\\{location}\\{layer}\\{layer_dirs}')
                    else:
                         if not(layer_dirs in os.listdir(f'{new_directory}\\{location}\\{layer}')):
                              shutil.copy2(dirs_paths_map2[layer] + f"\\{layer_dirs}", f'{new_directory}\\{location}\\{layer}')




if __name__ == "__main__":
     # copy_waypoints(dirs_paths_map1[3], dirs_paths_map2[3])
     # copy_the_nether(dirs_paths_map1[2], dirs_paths_map2[2])
     # copy_dimension(dirs_paths_map1[1], dirs_paths_map2[1], "the_end")
     # copy_dimension(dirs_paths_map1[0], dirs_paths_map2[0], "overworld")
     # copy_dimension(dirs_paths_map1[2], dirs_paths_map2[2], "the_nether")
     pass

