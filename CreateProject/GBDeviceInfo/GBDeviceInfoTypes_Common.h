//
//  GBDeviceInfoTypes_Common.h
//  GBDeviceInfo
//
//  Created by Luka Mirosevic on 20/02/2015.
//  Copyright (c) 2015 Luka Mirosevic. All rights reserved.
//
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//  http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.

#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>

typedef NS_ENUM(NSInteger, GBByteOrder) {
    GBByteOrderLittleEndian,
    GBByteOrderBigEndian,
};

typedef struct {
    /**
     Major OS version number. For e.g. 10.8.2 => 10
     */
    NSUInteger                                          major;
    
    /**
     Minor OS version number. For e.g. 10.8.2 => 8
     */
    NSUInteger                                          minor;
    
    /**
     Patch OS version number. For e.g. 10.8.2 => 2
     */
    NSUInteger                                          patch;
} GBOSVersion;

/**
 Makes a GBOSVersion struct.
 */
inline static GBOSVersion GBOSVersionMake(NSUInteger major, NSUInteger minor,  NSUInteger patch) {
    return (GBOSVersion){major, minor, patch};
};

typedef struct {
    /**
     Major device model. e.g. 13 for iMac13,2
     */
    NSUInteger                                          major;
    
    /**
     Minor device model. e.g. 2 for iMac13,2
     */
    NSUInteger                                          minor;
} GBDeviceVersion;

/**
 Makes a GBDeviceVersion struct.
 */
inline static GBDeviceVersion GBDeviceVersionMake(NSUInteger major, NSUInteger minor) {
    return (GBDeviceVersion){major, minor};
};

typedef struct {
    /**
     CPU frequency, in GHz.
     
     Warning: Might not be (=probably won't be) available on all iOS devices.
     */
    CGFloat                                             frequency;              // GHz (giga)
    
    /**
     Number of logical cores the CPU has.
     */
    NSUInteger                                          numberOfCores;
    
    /**
     CPU's l2 cache size, in KB.
     */
    CGFloat                                             l2CacheSize;            // KB (kibi)
} GBCPUInfo;

/**
 Makes a GBCPUInfo struct.
 */
inline static GBCPUInfo GBCPUInfoMake(CGFloat frequency, NSUInteger numberOfCores, CGFloat l2CacheSize) {
    return (GBCPUInfo){frequency, numberOfCores, l2CacheSize};
};
