from typing import Union, List, Tuple, Any, Callable
from operator import itemgetter
from dataset import DataSetItem
from dataset import DataSetInterface 
dict = {}

class DataSet(DataSetInterface):
    def __init__(self,items:Union[List[DataSetItem], Tuple[DataSetItem, ...]]=[]):
        super().__init__(self)
        self.to_diction = {}
        for i in items:
            self.to_diction[DataSetItem.name] = i
            
    def __setitem__(self, name:str, id_content:Tuple[int, Any]):
        item = DataSetItem(name,id_content[0],id_content[1])
        self.to_diction[name] = item
        
        
    def __iadd__(self, item:DataSetItem):
        self.to_diction[item.name] = item
        return self
    def __delitem__(self, name:str):
        self.to_diction.pop(name, None)
                
                
                
    def __contains__(self, name:str) -> bool:
        res = False
        for i in self.to_diction:
            if i == name:
                res =True
                break
        return res
        
    def __getitem__(self, name:str) -> DataSetItem:
        for i in self.to_diction:
            if i == name:
                return self.to_diction[i]
                
                
                
    def __getitem__(self, name:str) -> DataSetItem:
						return self.to_diction[name]


    def __and__(self, dataset:DataSetInterface) -> DataSetInterface:
	    dataset_diction={}
	    for i in dataset:
	        dataset_diction[i.name] = i
	        intersection = dataset_diction.keys() & self.to_diction.keys()
	        dict_intersection = {k: self.to_diction[k] for k in intersection }
	        return dict_intersection


    def __or__(self, dataset:DataSetInterface) -> DataSetInterface:
	    dataset_diction={}
	    dataset_diction_all={}
	    for i in dataset:
	        dataset_diction_all[i.name] = i
	        dataset_diction = self.to_diction | dataset_diction_all
        return dataset_diction
	        
    def __iter__(self):
        if not self.iterate_sorted:
            self.to_diction
        elif self.iterate_reversed:
            self.to_diction =dict(reversed(list(self.to_diction.items())))
        elif self.iterate_sorted and self.iterate_key == self.ITERATE_SORT_BY_NAME:
            sorted_keys = sorted(self.to_diction.keys())
            self.to_diction = {key:self.to_diction[key] for key in sorted_keys}
        elif self.iterate_sorted and self.iterate_key == self.ITERATE_SORT_BY_ID:
            self.to_diction = dict(sorted(self.to_diction.items(), key=lambda item: item[1]))
            
        for i in self.to_diction:
            yield self.to_diction[i]
    
    
    

    def filtered_iterate(self, filter:Callable[[str, int], bool]):
        filter_list=[]
        for item in self.items:
            if(filter(DataSetItem.name,DataSetItem.id)):
                filter_list.append(item)
        return iter(filter_list)
        
    def __len__(self) -> int:
        return len(self.to_diction)            
                
