import os
import shutil
import errno
import sys
import string
import Foundation, objc,AppKit
import uuid

#from mod_pbxproj import XcodeProject

NSMutableDictionary = objc.lookUpClass('NSMutableDictionary')
NSMutableArray = objc.lookUpClass('NSMutableArray')
NSDictionary = objc.lookUpClass('NSDictionary')
NSArray = objc.lookUpClass('NSArray')

ProjectName = 'Example'


class ProjectFileItem:

    def __init__(self,path):
        self.path = path
        self.project = NSMutableDictionary.dictionaryWithContentsOfFile_(path)


    def save(self):
        return self.project.writeToFile_atomically_(self.path +'tst',True)

    def getFileType(fileExtentsion):
        fileTypes = {
            'app':'wrapper.application',
            'a':'archive.ar',
            'octest':'wrapper.cfbundle'
        }
        return fileTypes(fileExtentsion)

    def addProject(projectFile):

        fileName = 'project.pbxproj'
        rootId = self.project.objectForKey_('rootObject')
        objects =  self.project.objectForKey_('objects')
        PBXProject = objects.objectForKey_(rootId)
        productRefGroupId = BXProject.objectForKey_('productRefGroup')
        PBXGroup = bjects.objectForKey_(productRefGroupId)

        ProductGroupId = createId()
        ProjectRefId = createId()
        PBXProject.setValue_forKey_([{'ProductGroup':ProductGroupId,'ProjectRef':ProjectRefId}],'projectReferences')


        fromProject = NSMutableDictionary.dictionaryWithContentsOfFile_(os.path.join(projectFile,fileName))
        fromRootId = fromProject.objectForKey_('rootObject')
        fromObjects =  fromProjectt.objectForKey_('objects')
        fromPBXProject = fromObjects.objectForKey_(fromRootId)
        fromProductRefGroupId = fromPBXProject.objectForKey_('productRefGroup')
        fromPBXGroup = fromObjects.objectForKey_(fromProductRefGroupId)
        children = [createId(),createId()]
        a = 0

        for child in fromPBXGroup.objectForKey_('children'):
            a++
            PBXFileReference = fromObjects.objectForKey_(child)
            referencePath = PBXFileReference.objectForKey_('path')
            baseName = os.path.basename(referencePath)
            name = baseName.split('.')[0]
            remoteRefId = createId()
            objects.setValue_forKey_({
                                         'isa':'PBXContainerItemProxy',
                                         'containerPortal':ProjectRefId,
                                         'proxyType','2',
                                         'remoteGlobalIDString':createId(),
                                         'remoteInfo'=name,
            },remoteRefId)

            objects.setValue_forKey_({
                                            'isa':'PBXReferenceProxy',
                                            'fileType':PBXFileReference.objectForKey_('explicitFileType'),
                                            'path': referencePath,
                                            'remoteRef':remoteRefId,
                                            'sourceTree':PBXFileReference.objectForKey_('sourceTree')
                                        },children[a])


        objects.setValue_forKey_({
                                        'isa':'PBXGroup',
                                        'children':children,
                                        'name':'Products',
                                        'sourceTree':'<group>'
                                        },ProductGroupId)



        objects.setValue_forKey_({
                                     'isa':'PBXFileReference',
                                     'lastKnownFileType','wrapper.pb-project',
                                     'name':os.path.basename(projectFile),
                                     'path':projectFile.replace(os.getcwd(),''),
                                     'sourceTree':'<group>'


        },ProjectRefId)





def copyDir(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
       # else:
            #raise OSError,("can't copy ,errno %d"%exc.errno)
def walkPath(arg,dirs,files):
    print(dirs)
    print(files)

def cleanPath(path,newProjectName):
      for obj in os.listdir(path):
          obj = os.path.join(path,obj)
          print('---------%s'%obj)
          if os.path.isdir(obj):
              newPath = obj.replace(ProjectName,newProjectName)
              os.rename(obj,newPath)
              print('newpath %s'%newPath)
              cleanPath(newPath,newProjectName)
          else:
                    if '.DS_Store' in obj:
                        continue
                    if 'pbxproj' in obj:
                        print('project file'+obj)
                    if '.h' in obj or '.m' in obj or '.pbxproj' in obj:
                        filePath = obj
                        try:
                            s = open(filePath).read()
                        except IOError:
                            print ("Could not open file! Please close Excel!")
                        else:
                            s = s.replace(ProjectName,newProjectName)
                            f = open(filePath, 'w')
                            f.write(s)
                            f.close()
                        if ProjectName+'Tests.m' in filePath:
                            os.rename(filePath,filePath.replace(ProjectName,newProjectName))

def addZxing(projectFile):
    currentPath = os.getcwd()
    zxingDir = os.path.join(currentPath,'zxing')
    if os.path.exists(zxingDir):
         project = NSMutableDictionary.dictionaryWithContentsOfFile_(projectFile)



         rootId = project.objectForKey_('rootObject')
         objects =  project.objectForKey_('objects')
         PBXProject = objects.objectForKey_(rootId)
         ProductGroup = createId()
         ProjectRef = createId()
         PBXProject.setValue_forKey_([{'ProductGroup':ProductGroup,'ProjectRef':ProjectRef}],'projectReferences')
         PBXReferenceProxy1 = createId()

         remoteRefId1 = createId()

         remoteRef1 = {
             'isa':'PBXContainerItemProxy',
             'containerPortal': ProjectRef,
             'proxyType' : '2',
             'remoteGlobalIDString' : createId(),
             'remoteInfo' : 'ZXingWidget',
         }
         objects.setValue_forKey_(remoteRef1,remoteRefId1)

         PBXReferenceProxy1Object = {
             'isa':'PBXReferenceProxy',
             'fileType':'archive.ar',
             'path':'libZXingWidget.a',
             'remoteRef':remoteRefId1,
             'sourceTree':'BUILT_PRODUCTS_DIR',
         }
         objects.setValue_forKey_(PBXReferenceProxy1Object,PBXReferenceProxy1)

         remoteRefId2 = createId()

         remoteRef2 = {
             'isa':'PBXContainerItemProxy',
             'containerPortal': ProjectRef,
             'proxyType' : '2',
             'remoteGlobalIDString' : createId(),
             'remoteInfo' : 'ZXingTests',
         }
         objects.setValue_forKey_(remoteRef2,remoteRefId2)

         PBXReferenceProxy2Object = {
             'isa':'PBXReferenceProxy',
             'fileType':'wrapper.cfbundle',
             'path':'ZXingTests.octest',
             'remoteRef':remoteRefId2,
             'sourceTree':'BUILT_PRODUCTS_DIR',
         }

         PBXReferenceProxy2 = createId()

         objects.setValue_forKey_(PBXReferenceProxy2Object,PBXReferenceProxy2)



         ProductGroupObject = {
             'isa':'PBXGroup',
             'children':[PBXReferenceProxy1,PBXReferenceProxy2],
             'name':'Products',
             'sourceTree':'<group>'
                               }
         objects.setValue_forKey_(ProductGroupObject,ProductGroup)

         ProjectRefObject = {
             'isa' : 'PBXFileReference',
             'lastKnownFileType' : 'wrapper.pb-project',
             'name' : 'ZXingWidget.xcodeproj',
             'path' :'zxing/iphone/ZXingWidget/ZXingWidget.xcodeproj',
             'sourceTree' : '<group>',
         }

         objects.setValue_forKey_(ProjectRefObject,ProjectRef)

         mainGroupId =  PBXProject.objectForKey_('mainGroup')
         PBXGroup = objects.objectForKey_(mainGroupId)
         children = PBXGroup.objectForKey_('children')
         children.insertObject_atIndex_(ProjectRef,0)

         project.writeToFile_atomically_(projectFile +'l',True)

         #添加Build Phase ZxingWidget依赖
         zxingWidgetDependencyId = createId()
         targets = PBXProject.objectForKey_('targets')
         projectTargetId = targets[0]
         print(projectTargetId)

         PBXNativeTarget = objects.objectForKey_(projectTargetId)
         dependencies = PBXNativeTarget.objectForKey_('dependencies')
         dependencies.addObject_(zxingWidgetDependencyId)


         targetProxyId = createId()

         zxingWidgetDependency = {
             'isa' : 'PBXTargetDependency',
             'name' : 'ZXingWidget',
             'targetProxy':targetProxyId,
         }
         objects.setValue_forKey_(zxingWidgetDependency,zxingWidgetDependencyId)

         targetProxy = {
             'isa' : 'PBXContainerItemProxy',
             'containerPortal' : ProjectRef,
             'proxyType' : '1',
             'remoteGlobalIDString': createId(),
             'remoteInfo' : 'ZXingWidget',
         }
         objects.setValue_forKey_(targetProxy,targetProxyId)

         #add libzxingwidget.a

         PBXBuildFileId = createId()
         objects.setValue_forKey_({'isa':'PBXBuildFile','fileRef':PBXReferenceProxy1},PBXBuildFileId)





         if project.writeToFile_atomically_(projectFile +'tst',True):
             print('save')






    else:
        print ('zxing not exist')


def createId():
    return ''.join(str(uuid.uuid4()).upper().split('-')[1:])



if __name__ == '__main__':


    #addZxing('/Users/virgil/Desktop/project.pbxproj')
    '''
    if len(sys.argv) > 1:
            newProjectName = sys.argv[1]
    else:
        newProjectName = 'testvv'
    currentPath = os.getcwd()
    projectDir = os.path.join(currentPath,ProjectName)
    if os.path.exists(projectDir) == False:
        print('Project File Not Exist')
    else:
        newProjectPath = os.path.join(currentPath,newProjectName)
        try:
            copyDir(projectDir,newProjectPath)
        except Exception, e:
            print (e)
        else:
            cleanPath(newProjectPath,newProjectName)
    '''


