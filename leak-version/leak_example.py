import tensorflow as tf
from memory_profiler import profile

FILE = 'gs://tensorflow-leak-test/file-{idx}.dcm'



@profile
def load_dicom(filename):
    with tf.gfile.GFile(filename, 'rb') as dicom_file_obj:
        return dicom_file_obj.read()


for i in range(0, 5):
    print(len(load_dicom(FILE.format(idx=i))))
