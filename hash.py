from linked_list import Node, SingleLinkedList

class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.buckets = []
        self._createHashTable()

    def _createHashTable(self):
        for i in range(self.size):
            self.buckets.append(SingleLinkedList())

    # 해시 함수 
    def hash_function(self, name):
        if name[0].isalpha():
            return ord(name.lower()[0]) % self.size

    # 링크드 리스트에 이름 전화번호 삽입 함수
    def add(self, name, mobile):
        # 1. 해시 함수로 버킷의 인덱스를 구함
        index = self.hash_function(name)
        # 2. 링크드 리스트로 이름/전화번호 삽입
        self.buckets[index].add_node(name, mobile)

    # 이름을 키로하여 전화 번호 조회 함수
    def get_mobile(self, name):
        index = self.hash_function(name)
        return self.buckets[index].find_by_name(name)

    # 이름을 키로하여 전화 번호 삭제 함수
    def delete(self, name):
        index = self.hash_function(name)
        self.buckets[index].remove_node(name)

    def print_hash_table(self):
        for i in range(self.size):
            if self.buckets[i].head is not None:
                print("{} Bucket: ".format(i))
                self.buckets[i].print_linked_list()
                print("")

def test_hash_table():
    hashtable.add('Anna', '010-1111-1111')
    hashtable.add('Anika', '010-1111-1112')
    hashtable.add('Becky', '010-1111-1113')
    hashtable.add('Billy', '010-1111-1114')
    hashtable.add('Caesar', '010-1111-1115')
    hashtable.add('Caley', '010-1111-1116')
    hashtable.add('david', '010-1111-1117')
    hashtable.add('donna', '010-2222-2228')
    hashtable.add('Evan', '010-1111-1119')
    hashtable.add('edward', '010-2222-2222')
    hashtable.add('Filia', '010-2222-2223')
    hashtable.add('Fella', '010-2222-2224')
    hashtable.add('Gabriel', '010-2222-2225')
    hashtable.add('Gali', '010-2222-2226')
    hashtable.add('Haley', '010-2222-2227')
    hashtable.add('Harry', '010-2222-2228')
    hashtable.add('Ian', '010-2222-2229')
    hashtable.add('Indira', '010-3333-3333')

if __name__ == "__main__":

    # 전화 번호 삽입 구현 확인
    hashtable = HashTable(26)
    test_hash_table()
    hashtable.print_hash_table()

    # 전화 번호 조회 구현 확인
    print("get david mobile = ", end=""), print( hashtable.get_mobile('david') )
    print("get donna mobile = ", end=""), print( hashtable.get_mobile('donna') )

    # 저장 안된 사람 전화 번호 조회 구현 확인
    print("donna2 mobile = ", end=""), print( hashtable.get_mobile('donna2') )

    # 전화 번호 삭제 구현 확인
    print("delete donna mobile = ", end=""), print( hashtable.delete('donna') )    
    hashtable.print_hash_table()
